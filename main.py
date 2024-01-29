"""Coffee Machine"""
import config
import sys

# Information about drinks
COFFEE_DRINKS = [
    {"number": 1, "name": "espresso", "coffee": 18, "water": 50, "milk": 0, "cost": 1.5},
    {"number": 2, "name": "latte", "coffee": 24, "water": 100, "milk": 150, "cost": 2.5},
    {"number": 3, "name": "cappuccino", "coffee": 24, "water": 150, "milk": 100, "cost": 2},]

# Setting flags
machine_off = False
manager_mode = False

# Setting measures of liquids for different coffee drinks and intializing revenue
current_water = 300
current_coffee = 100
current_milk = 200

revenue = 0


def sanitize_input(number):
    """Does a type check and checks if the number is in the right range."""
    if not number.isnumeric():
        print(config.DRINK_ERROR_MESSAGE)
        sys.exit(0)
    else:
        number = int(number)
        if number > 3 or number <= 0:
            print(config.DRINK_ERROR_MESSAGE)
            sys.exit(0)

    return number


def get_data(drink_number, lst):
    """Extracts information about a certain drink from a dictionary by its index."""
    drink_number = sanitize_input(drink_number)

    drink_dict = lst[drink_number - 1]
    water_amount = drink_dict["water"]
    coffee_amount = drink_dict["coffee"]
    milk_amount = drink_dict["milk"]
    cost = drink_dict["cost"]

    return water_amount, coffee_amount, milk_amount, cost


def subtract_measures(tpl):
    """Imitates preparing a coffee by subtracting a necessary amount of water, coffee and milk from the supplies."""
    global current_water, current_coffee, current_milk
    current_water -= tpl[0]
    current_coffee -= tpl[1]
    current_milk -= tpl[2]

    return current_water, current_coffee, current_milk


def check_measures(data):
    """Checks if there is enough supplies to make a drink."""
    water, coffee, milk = data[0], data[1], data[2]
    global current_water, current_coffee, current_milk
    return water > current_water or coffee > current_coffee or milk > current_milk


def count_money():
   """Takes a number of coins of different values and returns their summary."""
   while True:
       # Loop until all inputs are valid
       valid_input = True

       # Validate and assign each input
       pennies = get_valid_int(config.ASK_FOR_PENNIES)
       nickels = get_valid_int(config.ASK_FOR_NICKELS)
       dimes = get_valid_int(config.ASK_FOR_DIMES)
       quarters = get_valid_int(config.ASK_FOR_QUARTERS)

       # Check if any input was invalid
       if not valid_input:
           print("Invalid input. Please enter positive integers for the number of coins.")
           continue  # Restart the loop

       # All inputs valid, exit the loop
       break

   # Perform calculations and return total money
   pennies *= 0.01
   nickels *= 0.05
   dimes *= 0.1
   quarters *= 0.25

   money = pennies + nickels + dimes + quarters

   return money

# Helper function to validate and get positive integer input
def get_valid_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            else:
                raise ValueError
        except:
            ValueError


def subtract_money(tpl, money):
    """Subtracts cost of the drink from given money and returns change."""
    change = money - tpl[3]
    return change


def is_transaction_successful(change):
    """Returns true if change is bigger than 0."""
    return change >= 0


def process_order():
    """Processes the order. Prompts user to choose a drink. Prepares it if there are enough supplies
    and the transaction was successful. If the user types 'manager', enters the manager mode. The manager can see the
    report, which includes current supplies and revenue. The manager can turn off the coffee machine"""
    global manager_mode
    global current_water, current_coffee, current_milk, revenue
    user_drink = input(config.ASK_FOR_COFFEE).lower()
    if user_drink == "manager":
        manager_mode = True
        return

    # Get information about the drink and make the drink
    drink_data = get_data(user_drink, COFFEE_DRINKS)
    not_enough_supplies = check_measures(drink_data)
    if not_enough_supplies:
        print(config.NOT_ENOUGH_SUPPLIES)
        return

    current_water, current_coffee, current_milk = subtract_measures(drink_data)

    given_money = count_money()
    print(f"You inserted ${given_money}.")
    user_change = subtract_money(drink_data, given_money)
    if user_change > 0:
        print(f"Here is your change: ${user_change}.")

    # Check if the transaction was successful
    if is_transaction_successful(user_change):
        revenue += drink_data[3]  # Add the cost of the drink to revenue
        print(config.GIVE_COFFEE)
        print(config.CUP_OF_COFFEE)
    else:
        print(config.ASK_FOR_MORE_MONEY)


while not machine_off:
    process_order()

    while manager_mode:
        manager_functions = input(config.MANAGER_MODE)

        manager_functions = sanitize_input(manager_functions)

        if manager_functions == 1:
            # Report about the amount of milk, water, and coffee
            print(
                f"There are {current_water}ml of water, {current_coffee}g of coffee, and {current_milk}ml of milk left."
                f"The revenue is ${revenue}.")
        elif manager_functions == 2:
            # Exit the loop
            manager_mode = False
        elif manager_functions == 3:
            machine_off = True
            break
