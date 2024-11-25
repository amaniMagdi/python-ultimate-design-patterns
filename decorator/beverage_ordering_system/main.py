from tea import Tea
from coffee import Coffee
from milk_decorator import MilkDecorator
from mint_decorator import MintDecorator
from sugar_decorator import SugarDecorator

def main():
    # Test plain Tea
    tea = Tea()
    print("Plain Tea:", tea.prepare())

    # Tea with Milk
    milk_tea = MilkDecorator(tea)
    print("Milk Tea:", milk_tea.prepare())

    # Tea with Milk and Mint
    milk_mint_tea = MintDecorator(milk_tea)
    print("Milk and Mint Tea:", milk_mint_tea.prepare())

    # Tea with Milk, Mint, and Sugar
    milk_mint_sugar_tea = SugarDecorator(milk_mint_tea)
    print("Milk, Mint, and Sugar Tea:", milk_mint_sugar_tea.prepare())

    # Test plain Coffee
    coffee = Coffee()
    print("Plain Coffee:", coffee.prepare())

    # Coffee with Milk
    milk_coffee = MilkDecorator(coffee)
    print("Milk Coffee:", milk_coffee.prepare())

    # Coffee with Milk and Sugar
    milk_sugar_coffee = SugarDecorator(milk_coffee)
    print("Milk and Sugar Coffee:", milk_sugar_coffee.prepare())

    # Coffee with Milk, Mint, and Sugar
    milk_mint_sugar_coffee = MintDecorator(milk_sugar_coffee)
    print("Milk, Mint, and Sugar Coffee:", milk_mint_sugar_coffee.prepare())

if __name__ == "__main__":
    main()
