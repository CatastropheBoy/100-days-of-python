from turtle import Turtle, Screen
from prettytable import PrettyTable

# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("DarkSalmon")
# timmy.forward(100)
# my_screen = Screen()
# my_screen.exitonclick()

table = PrettyTable()
table.add_column("Pokemon", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)