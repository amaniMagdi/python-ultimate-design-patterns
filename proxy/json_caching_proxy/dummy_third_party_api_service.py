import time
import requests
from dummy_json_api import DummyJsonApi

class DummyThirdPartyApiService(DummyJsonApi):
    PRODUCTS_ENDPOINT = "https://dummyjson.com/products"
    RECIPES_ENDPOINT = "https://dummyjson.com/recipes"

    def __init__(self):
        pass

    def get_all_products(self) -> str:
        try:
            print("Fetching products...")
            time.sleep(2)  # Simulates delay
            response = requests.get(self.PRODUCTS_ENDPOINT)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
            return response.text  # Returns the raw response body as a string
        except requests.RequestException as e:
            raise RuntimeError(f"Failed to fetch products: {e}")

    def get_all_recipes(self) -> str:
        try:
            print("Fetching recipes...")
            time.sleep(2)  # Simulates delay
            response = requests.get(self.RECIPES_ENDPOINT)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
            return response.text  # Returns the raw response body as a string
        except requests.RequestException as e:
            raise RuntimeError(f"Failed to fetch recipes: {e}")
