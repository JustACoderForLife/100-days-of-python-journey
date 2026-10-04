print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = float(input("What is your age in years? "))

if height >= 120:
    print("You can ride the rollercoaster")
    if age <=12:
        print("$5")
    elif age <=18:
        print("$7")
    else:
        print("$12")
else:
    print("Sorry you have to grow taller before you can ride.")
