from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
maker = CoffeeMaker()
money = MoneyMachine()

is_on = True
while is_on:
    print("Welcome to the Coffeetron 5000.")
    order = input(
        f"What would you like? {menu.get_items()}?").lower()
    if order == "off":
        is_on = False
    elif order == "report":
        maker.report()
        money.report()
    else:
        drink = menu.find_drink(order)
        if drink is not None:
            if maker.is_resource_sufficient(drink) and money.make_payment(drink.cost):
                maker.make_coffee(drink)
                    


