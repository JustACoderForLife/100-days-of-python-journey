import data
def getting_input(prompt, type):
    while True:
        try:
            return type(input(prompt))
        except ValueError:
            print(f"Invalid input. Please enter a valid {type.__name__}.")
def choice_of_drink():
    return getting_input("What would you like? (espresso/latte/cappuccino):", str)
def paying():
    print("Please enter coins.")
    quarters = getting_input("How many quarters would you like to enter: ", int)
    dimes = getting_input("How many dimes would you like to enter: ", int)
    nickels = getting_input("How many nickels would you like to enter: ", int)
    pennies = getting_input("How many pennies would you like to enter: ", int)
    money = (quarters*0.25)+(dimes*0.10)+(nickels*0.05)+(pennies*0.01)
    return money
program_over = False

while not program_over:
    can_make_drink = True
    choice = choice_of_drink()
    if choice == "off":
        program_over = True
    elif choice == "report":
        print(f"Water: {data.resources['water']}ml")
        print(f"Milk: {data.resources['milk']}ml")
        print(f"Coffee: {data.resources['coffee']}g")
        print(f"Money: ${data.resources['money']}")
    elif choice in data.MENU:
        for ingredients in data.MENU[choice]["ingredients"]:
            if data.MENU[choice]["ingredients"][ingredients] > data.resources[ingredients]:
                print(f"Sorry. There is not enough {ingredients}")
                can_make_drink = False
        if can_make_drink:
            payment = paying()
            if payment < data.MENU[choice]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                for ingredients in data.MENU[choice]["ingredients"]:
                    data.resources[ingredients] -= data.MENU[choice]["ingredients"][ingredients]
                if payment > data.MENU[choice]["cost"]:
                    change = round(payment - data.MENU[choice]["cost"], 2)
                    print(f"Here is ${change} in change.")
                print(f"Here is your {choice} Enjoy!")
                data.resources["money"] += data.MENU[choice]["cost"]
                