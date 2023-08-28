import enum
import math
from typing import List

from celebrationData import EventScores
from citydata import CityInfo

class Category(enum.Enum):
    ALCOHOL = "alcohol"
    STAPLES = "staples"
    CLOTHING = "clothing"
    CONFECTIONARY = "confectionary"
    SEASONAL = "seasonal"
    BREAKFAST = "breakfast"
    SNACKS = "snacks"
    FROZEN = "frozen"
    DAIRY = "dairy"

class WeightedProduct():
    name: str
    category: str
    price: float
    occurrence: float
    temp_weight: float
    thanksgiving_weight: float
    xmas_weight: float
    easter_weight: float
    valentines_weight: float
    halloween_weight: float
    new_year_weight: float

class day_score():
    day: int
    spend_weight: float
    temp_weight: float
    thanksgiving_weight: float
    xmas_weight: float
    easter_weight: float
    valentines_weight: float
    halloween_weight: float
    new_year_weight: float


class buy_calcuation():
    amount_to_spend: float
    time_of_year: int

def calculate_day_score(time_of_year: int, city:  CityInfo, event_scores: EventScores) -> day_score:
    my_day = day_score()
    my_day.spend_weight = city.GDP * city.population
    my_day.day = time_of_year
    my_day.temp_weight = city.temp_per_day[time_of_year]
    my_day.thanksgiving_weight = city.thanksgiving_weight * event_scores.thanksgiving_weight[time_of_year]
    my_day.xmas_weight = city.xmas_weight * event_scores.xmas_weight[time_of_year]
    my_day.easter_weight = city.easter_weight * event_scores.easter_weight[time_of_year]
    my_day.valentines_weight = city.valentines_weight * event_scores.valentines_weight[time_of_year]
    my_day.halloween_weight = city.halloween_weight * event_scores.halloween_weight[time_of_year]
    my_day.new_year_weight = city.new_year_weight * event_scores.new_year_weight[time_of_year]
    return my_day


