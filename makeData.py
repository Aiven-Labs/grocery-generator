import datetime
import json
import random
from pprint import pprint

import aiokafka
from aiokafka import AIOKafkaProducer
import asyncio

from aiokafka.helpers import create_ssl_context
from pydantic import BaseModel
from snowflake.snowflake import SnowflakeGenerator

from celebrationData import make_my_event_scores
from citydata import make_my_cities
from groceryLists import GroceryList
from product_values import calculate_day_score

import numpy as np
from noise import snoise2

import config
context = create_ssl_context(
    cafile="certificates/ca.pem",
    certfile="certificates/service.cert",
    keyfile="certificates/service.key",
)

TOPIC_NAME = "input-events"

def generate_simplex_noise(period, num_values, amplitude=1, seed=0, octaves=1, persistence=0.5):
    noise_values = np.zeros(num_values)
    frequency = 1 / period

    for i in range(num_values):
        noise_value = 0
        amplitude_i = amplitude

        for _ in range(octaves):
            noise_value += amplitude_i * snoise2(seed + i * frequency, seed)
            frequency *= 2
            amplitude_i *= persistence

        noise_values[i] = noise_value
    return noise_values


class Purchase(BaseModel):
    id: int
    city: str
    item: str
    price: float
    influencer: str = None


class Basket(BaseModel):
    id: int
    city: str
    purchase_day: int
    total_purchases: int
    purchases: list[Purchase]
    pass


def  get_random_item_from_dict(my_dict):
    return random.choice(list(my_dict.items()))


def seeded_random(seed):
    random.seed(seed)
    while True:
        yield random.random()


async def my_loop(my_producer):
    topic_name = "CDC-input"
    producer = my_producer
    random_gen = seeded_random(42)
    period = 365
    num_values = 365
    amplitude = 1
    seed = 42
    octaves = 3
    persistence = 0.5
    id_gen = SnowflakeGenerator(42)
    basket_id = SnowflakeGenerator(420)

    my_cities = make_my_cities()
    city_seed = 42
    for key, value in my_cities.items():
        city_seed += 1
        my_cities[key].noise_values = generate_simplex_noise(period, num_values, amplitude, city_seed, octaves, persistence)

    simplex_noise_values = generate_simplex_noise(period, num_values, amplitude, seed, octaves, persistence)

    my_events = make_my_event_scores()

    my_groceries = GroceryList()

    purchases_per_day = 5000
    newyear_purchases = 0
    easter_purchases = 0
    thanksgiving_purchases = 0
    xmas_purchases = 0
    halloween_purchases = 0

    total_purchases = 0

    start_date = datetime.datetime(2020, 1, 1) + datetime.timedelta(hours=3.4)
    for day in range(365):
        for city in my_cities.values():

            my_score = calculate_day_score(day, city, my_events)
            holiday_weighting = ((1 + my_score.xmas_weight) *
                                 (1 + my_score.thanksgiving_weight) *
                                 (1 + my_score.easter_weight) *
                                 (1 + my_score.halloween_weight) *
                                 (1 + my_score.new_year_weight))
            weighted_purchases = my_score.spend_weight * (
                    city.noise_values[day] + 1) * purchases_per_day * holiday_weighting
            daily_purchases = []
            current_day = start_date + datetime.timedelta(days=day)

            while weighted_purchases > 0:
                current_day = current_day + datetime.timedelta(
                    seconds=(max(86400, (86400 / (min(weighted_purchases, 1))))))
                basket_size = max(round(random.gauss(25 * holiday_weighting, 12 * ((1 + holiday_weighting) / 2))),
                                  2) + 2
                my_basket = Basket(id=next(basket_id), city=city.name, purchase_day=current_day.timestamp(),
                                   purchases=[], total_purchases=basket_size)

                for basket_item in range(basket_size):
                    if weighted_purchases <= 0:
                        break
                    weighted_purchases -= 1
                    purchase = Purchase(id=next(id_gen), city="city", item="item", price=10)
                    purchase.city = city.name
                    purchase.item, purchase.price = get_random_item_from_dict(my_groceries.general)

                    daily_purchases.append(purchase.json())
                    my_basket.purchases.append(purchase)
                    if random_gen.__next__() < my_score.xmas_weight:
                        next_item, next_price = get_random_item_from_dict(my_groceries.xmas)
                        xmas_purchase = Purchase(id=next(id_gen), city=city.name,
                                                 item=next_item,
                                                 price=next_price,
                                                 influencer="xmas")
                        daily_purchases.append(xmas_purchase.json())
                        my_basket.purchases.append(xmas_purchase)

                        weighted_purchases -= 1
                        xmas_purchases += 1

                    if random_gen.__next__() < my_score.thanksgiving_weight:
                        next_item, next_price = get_random_item_from_dict(my_groceries.thanksgiving)
                        thanksgiving_purchase = Purchase(id=next(id_gen), city=city.name,
                                                         item=next_item,
                                                         price=next_price,
                                                         influencer="thanksgiving")
                        daily_purchases.append(thanksgiving_purchase.json())
                        my_basket.purchases.append(thanksgiving_purchase)
                        weighted_purchases -= 1
                        thanksgiving_purchases += 1

                    if random_gen.__next__() < my_score.easter_weight:
                        next_item, next_price = get_random_item_from_dict(my_groceries.easter)
                        easter_purchase = Purchase(id=next(id_gen), city=city.name, item=next_item,
                                                   price=next_price,
                                                   influencer="easter")
                        daily_purchases.append(easter_purchase.json())
                        my_basket.purchases.append(easter_purchase)
                        weighted_purchases -= 1
                        easter_purchases += 1

                    if random_gen.__next__() < my_score.valentines_weight:
                        next_item, next_price = get_random_item_from_dict(my_groceries.valentines)
                        valentines_purchase = Purchase(id=next(id_gen), city=city.name, item=next_item,
                                                       price=next_price)

                        daily_purchases.append(valentines_purchase.json())
                        my_basket.purchases.append(valentines_purchase)
                        weighted_purchases -= 1

                    if random_gen.__next__() < my_score.new_year_weight:
                        next_item, next_price = get_random_item_from_dict(my_groceries.new_year)
                        new_year_purchase = Purchase(id=next(id_gen), city=city.name, item=next_item,
                                                     price=next_price,
                                                     influencer="new_year")
                        daily_purchases.append(new_year_purchase.json())
                        my_basket.purchases.append(new_year_purchase)
                        weighted_purchases -= 1
                        newyear_purchases += 1
                        pass
                    pass
                await producer.send(topic_name, my_basket.json().encode("utf-8"))

            total_purchases += len(daily_purchases)
            json_purchases = json.dumps(daily_purchases)

async def main():
    global producer
    producer = aiokafka.AIOKafkaProducer(
        bootstrap_servers=config.KAFKA_URI,
        security_protocol="SSL",
        ssl_context=context
    )

    await producer.start()
    await my_loop(producer)
    await producer.stop()


asyncio.run(main())
