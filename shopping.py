items = {
    "Milk": 50,
    "Bread": 40,
    "Eggs": 120,
    "Rice": 60,
    "Sugar": 45
}

cart = ["Milk", "Eggs", "Rice"]

total = 0

print("🛒 Shopping Bill")
print("----------------")

for item in cart:
    price = items[item]
    total += price
    print(item, ":", price)

# discount logic
discount = 0
if total >= 200:
    discount = total * 0.10

final_amount = total - discount

print("\nSubtotal:", total)
print("Discount:", discount)
print("Amount to Pay:", final_amount)
