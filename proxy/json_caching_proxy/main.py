from dummy_json_caching_proxy import DummyJsonCachingProxy

def main():
    # Create an instance of the caching proxy
    proxy = DummyJsonCachingProxy()

    # First call to get_all_products (should fetch from API and cache it)
    print("First call to get_all_products (fetch from API):")
    products = proxy.get_all_products()
    print(products[:100] + "...")  # Print first 100 characters for brevity

    # Second call to get_all_products (should fetch from cache)
    print("\nSecond call to get_all_products (fetch from cache):")
    products_cached = proxy.get_all_products()
    print(products_cached[:100] + "...")  # Print first 100 characters for brevity

    # First call to get_all_recipes (should fetch from API and cache it)
    print("\nFirst call to get_all_recipes (fetch from API):")
    recipes = proxy.get_all_recipes()
    print(recipes[:100] + "...")  # Print first 100 characters for brevity

    # Second call to get_all_recipes (should fetch from cache)
    print("\nSecond call to get_all_recipes (fetch from cache):")
    recipes_cached = proxy.get_all_recipes()
    print(recipes_cached[:100] + "...")  # Print first 100 characters for brevity

if __name__ == "__main__":
    main()
    