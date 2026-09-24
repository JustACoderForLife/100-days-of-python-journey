# import turtle
# import prettytable

# timmy = turtle.Turtle()
# print(timmy)
# my_screen = turtle.Screen()
# print(my_screen.canvheight)
# timmy.shape("turtle")
# timmy.color("aquamarine")
# timmy.forward(100)
# my_screen.exitonclick()
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
