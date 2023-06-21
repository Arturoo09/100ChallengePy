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

profit = 0


def menu():
    print("\n\t** Welcome to the Coffee Machine Intelligence **\n")
    print("Options:\n")
    print("\t1. espresso")
    print("\t2. latte")
    print("\t3. cappuccino")
    print("\t4. report")


def report():
    for item in resources:
        print(f"{item}: {resources[item]}")


def are_resources(resource):
    for item in resource:
        if resource[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    print("🤑🤑🤑🤑")
    total = float(input("How many are u going to insert: "))
    return total


def is_transaction_succesful(money, drink_cost):
    if money >= drink_cost:
        change = round(money - drink_cost, 2)
        print(f"Here is {change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. The money was refunded!")
        return False


def make_coffee(coffee, coffe_ingredients):
    for item in coffe_ingredients:
        resources[item] -= coffe_ingredients[item]
    print(f"Here is your {coffee}☕️. Enjoy")


while True:
    menu()
    option = input("\nWhat would you like?: ")

    if option == "report":
        report()
    elif option == "off":
        print("\nExiting the Coffee Machine...")
        break
    else:
        drink = MENU[option]
        if are_resources(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_succesful(payment, drink["cost"]):
                make_coffee(option, drink["ingredients"])
