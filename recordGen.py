import random
import json
from typing import List, Dict, Any

from demoData.groceries import GroceryStore


class PurchaseRecordResult:
    def __init__(self, store: str, region: str, products: Dict[str, int], price_total: float):
        self.store: str = store
        self.region: str = region
        self.products: Dict[str, int] = products
        self.price_total: float = price_total


class PurchaseRecord:
    def __init__(self, stores_file_path: str, grocery_file_path: str, cereal_file_path: str):
        with open(stores_file_path, "r") as f:
            self.stores: Dict[str, List[str]] = json.load(f)["stores"]
        self.grocery_store: GroceryStore = GroceryStore(grocery_file_path)

    def get_product_price(self, product: str) -> float:
        if product in self.grocery_store.GROCERY_PRODUCTS:
            return self.grocery_products[product]
        else:
            raise ValueError(f"Product {product} not found in grocery or cereal products")

    def get_random_purchase_record(self) -> PurchaseRecordResult:
        region: str = random.choice(list(self.stores.keys()))
        store: str = random.choice(list(self.stores[region]))
        products: Dict[str, int] = {}
        num_products: int = random.randint(1, 25)
        for i in range(num_products):
            product_type: str = random.choice(["grocery", "cereal"])
            if product_type == "grocery":
                product_name, product_price = self.grocery_store.get_random_grocery()
            else:
                product_name, product_price = self.grocery_store.get_random_cereal()
            if product_name not in products:
                products[product_name] = 0
            products[product_name] += 1

        return PurchaseRecordResult(store=store, region=region, products=products, price_total=sum(
            self.products[product] * self.get_product_price(product)
            for product in self.products
        ))
