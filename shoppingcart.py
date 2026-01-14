foods= []
prices = []
total = 0

while True:
    food = input("enter a food to buy(q to quit): ")
    if  food.lower() == "q":
        break
    else :
        price = float(input(f"enter price of a {food}: "))
        foods.append(food)
        prices.append(price)

print("---YOUR CART---")

for food in foods:
    print(food)

for price in prices:
    total += price

print(f"your total is {total}")