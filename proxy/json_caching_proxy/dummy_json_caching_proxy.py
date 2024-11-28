from dummy_json_api import DummyJsonApi
from dummy_third_party_api_service import DummyThirdPartyApiService

class DummyJsonCachingProxy(DummyJsonApi):
    """
    This class is a proxy to the DummyJsonApi class.
    It is used to cache the responses to the API calls.
    """
    PRODUCTS_ENDPOINT = "https://dummyjson.com/products"
    RECIPES_ENDPOINT = "https://dummyjson.com/recipes"

    def __init__(self):
        self.dummy_json_api = DummyThirdPartyApiService()
        self.caching_layer= {}

    def get_all_products(self) -> str:
        if "PRODUCTS_ENDPOINT" in self.caching_layer:
            return self.caching_layer["PRODUCTS_ENDPOINT"]
        
        product_response = self.dummy_json_api.get_all_products()
        self.caching_layer["PRODUCTS_ENDPOINT"] = product_response
        return product_response

    def get_all_recipes(self) -> str:
        if "RECIPES_ENDPOINT" in self.caching_layer:
            return self.caching_layer["RECIPES_ENDPOINT"]
        
        recipes_response = self.dummy_json_api.get_all_recipes()
        self.caching_layer["RECIPES_ENDPOINT"] = recipes_response
        return recipes_response
