import main
# 1 cent = 0.01, 10 cents = 0.1, Nickel = 0.05, Quarter = 0.25

money_balance = 0
can_make = True
def mechanisms(water_amount_required, milk_amount_required, coffee_amount_required):
    main.resources['water'] -= water_amount_required
    main.resources['milk'] -= milk_amount_required
    main.resources['coffee'] -= coffee_amount_required

while can_make:
    drink = input("What would you like (espresso/latte/cappuccino/report): ").lower()

    if drink == "report":
        for key, value in main.resources.items():
            print(f"{key.capitalize()}: {value}ml")
        print(f"Money: ${money_balance}")
    elif (drink == "espresso") or (drink == "latte") or (drink == "cappuccino"):
        ingredients = main.MENU[drink]['ingredients']
        water_amount_required = ingredients.get('water', 0)
        milk_amount_required = ingredients.get('milk', 0)
        coffee_amount_required = ingredients.get('coffee', 0)

        if ((water_amount_required <= main.resources['water']) and
                (milk_amount_required <= main.resources['milk']) and
                (coffee_amount_required <= main.resources['coffee'])):
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            balance = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickels) + (0.01 * pennies)
            if balance > main.MENU[drink]['cost']:
                changes = balance - main.MENU[drink]['cost']
                money_balance += main.MENU[drink]['cost']
                print(f"Here is ${changes:.2f} in change.")
                print(f"Here is your {drink}. Enjoy!")
                mechanisms(water_amount_required, milk_amount_required, coffee_amount_required)
            elif balance == main.MENU[drink]['cost']:
                money_balance += main.MENU[drink]['cost']
                print("There is no changes")
                print(f"Here is your {drink}. Enjoy!")
                mechanisms(water_amount_required, milk_amount_required, coffee_amount_required)
            else:
                can_make = False
                print("There is not enough money.")
        else:
            can_make = False
            print("The drink is not available, as we are out of resources")

    else:
        can_make = False
        print("That drink isn't on the menu.")
