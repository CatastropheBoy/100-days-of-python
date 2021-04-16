MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0

def check_resources():
    return resources


def print_report():
    r = check_resources()
    print(f'Water: {r["water"]}ml\nMilk: {r["milk"]}ml\nCoffee: {r["coffee"]}g\nMoney: {money}')


def select_drink():
    print("Welcome to the Coffeetron 5000.")
    drink = input("What would you like? Espresso, Latte, or Cappuchino?").lower()
    if drink == "off":
        exit()
    if drink == "report":
        print_report()
        select_drink()
    elif drink not in MENU:
        print(f"{drink} is not a valid selection, please try again.")
        select_drink()
    else:
        process_coins(drink)


def process_coins(drink):
    quarters = float(input("How many quarters?: \n")) * 0.25
    dimes = float(input("How many dimes?: \n")) * 0.1
    nickels = float(input("How many nickels?: \n")) * 0.05
    pennies = float(input("How many pennies?: \n")) * 0.01
    cash = quarters + dimes + nickels + pennies
    drink_cost = MENU[drink]["cost"]

    if cash < drink_cost:
        print(f"Sorry that's not enough money. Money refunded.")
        select_drink()
    else:
        refund = cash - drink_cost
        if refund > 0:
            print(f"Here is ${refund} dollars in change.")
        add_money(drink_cost)
        make_drink(drink)


def make_drink(drink):
    order = MENU[drink]
    resources = check_resources()
    insufficient_resources = False
    for r in order["ingredients"]:
        if order["ingredients"][r] > resources[r]:
            print(f"Sorry there is not enough {r}")
            insufficient_resources = True
    if not insufficient_resources:
        for r in order["ingredients"]:
            a = order["ingredients"][r]
            use_resources(r, a)
        print(f"Here is your {drink}. Enjoy!")
    select_drink()


def add_money(cash):
    global money
    money += cash


def use_resources(resource, amount):
    global resources
    resources[resource] -= amount

select_drink()






