print("Welcome to Ryan's Coffee Shop!")

name = input("It's good to see you! What is your name? ")
print("Thank you,", name, "!")

drinks = ["Coffee", "Latte", "Mocha"]
flavors = ["plain", "caramel", "vanilla", "hazelnut", "pumpkin spice"]
toppings = ["chocolate", "cinnamon", "whipped cream", "caramel"]

print()
print("Our Drinks")
print("----------")
i = 1
for d in drinks:
    print(i, d)
    i += 1
drink = input("Please enter the number of the drink you'd like: ")

print()
print("Our Flavors")
print("------------")
i = 1
for f in flavors:
    print(i, f)
    i += 1
flavor = input("Please enter the number of the flavor you'd like: ")

print()
print("Our Toppings")
print("-------------")
i = 1
for t in toppings:
    print(i, t)
    i += 1
topping = input("Please enter the number of the topping you'd like: ")

print()
print("Here is your order: ")
print("Drink:", drinks[int(drink) - 1])
print("Flavor:", flavors[int(flavor) - 1])
print("Topping:", toppings[int(topping) - 1])
print("Thank you for your order!")
print("We'll call your name when it's ready,", name, "!")

