import json
import random


class GroceryStore:
    def __init__(self, filename):
        with open(filename) as f:
            data = json.load(f)
        self.GROCERY_PRODUCTS = data["products"]
        self.GROCERY_STORES = data["stores"]

    def get_random_product(self):
        product, price = random.choice(list(self.GROCERY_PRODUCTS.items()))
        return {"product": product, "price": price}

    def get_random_store_in_region(self, region):
        stores_in_region = self.GROCERY_STORES.get(region)
        if stores_in_region:
            return random.choice(stores_in_region)
        else:
            return None