"""Coffee Machine"""
import config
import sys

COFFEE_DRINKS = [
    {"number": 1,
     "name": "espresso",
     "coffee": 18,
     "water": 50,
     "milk": 0,
     "cost": 1.5},
    {"number": 2,
     "name": "latte",
     "coffee": 24,
     "water": 100,
     "milk": 150,
     "cost": 1.5},
    {"number": 3,
     "name": "cappuccino",
     "coffee": 24,
     "water": 150,
     "milk": 100,
     "cost": 1.5},
]

# TODO: 1. Set measures of liquids for different coffee drinks
current_water = 300
current_coffee = 100
current_milk = 200


def get_data(drink_number, lst):

    # Input sanitizing
    if not drink_number.isnumeric():
        print(config.DRINK_ERROR_MESSAGE)
        sys.exit(0)
    else:
        drink_number = int(user_drink)
        if drink_number > 3 or drink_number <= 0:
            print(config.DRINK_ERROR_MESSAGE)
            sys.exit(0)

    drink_dict = lst[drink_number-1]
    water_amount = drink_dict["water"]
    coffee_amount = drink_dict["coffee"]
    milk_amount = drink_dict["milk"]
    cost = drink_dict["cost"]

    return water_amount, coffee_amount, milk_amount, cost


# TODO: . Subtract a needed amount of supplies for the drink
def subtract_measures(tpl):
    global current_water, current_coffee, current_milk
    current_water -= tpl[0]
    current_coffee -= tpl[1]
    current_milk -= tpl[2]

    return current_water, current_coffee, current_milk


# TODO: . Manage money and give change if necessary (before making the drink)
def count_money():
    pennies = int(input(config.ASK_FOR_PENNIES))
    nickels = int(input(config.ASK_FOR_NICKELS))
    dimes = int(input(config.ASK_FOR_DIMES))
    quarters = int(input(config.ASK_FOR_QUARTERS))

    pennies *= 0.01
    nickels *= 0.05
    dimes *= 0.1
    quarters *= 0.25

    money = pennies + nickels + dimes + quarters

    return money


def subtract_money(tpl, money):
    change = money - tpl[3]
    return change


# TODO: . Check if the transaction was successful
def is_transaction_successful():
    pass


# TODO: . Ask the customer to choose a drink
user_drink = input(config.ASK_FOR_COFFEE)

# TODO:
drink_data = get_data(user_drink, COFFEE_DRINKS)
coffee = subtract_measures(drink_data)


given_money = count_money()
print(given_money)
user_change = subtract_money(drink_data, given_money)
print(user_change)

# TODO: 2. Report about the amount of milk, water, and coffee
print(f"There are {current_water}ml of water, {current_coffee}g of coffee, and {current_milk}ml of milk left.")