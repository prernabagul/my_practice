items = {
    "Milk": 50,
    "Bread": 40,
    "Eggs": 120,
    "Rice": 60,
    "Sugar": 45
}

# item : quantity
cart = {
    "Milk": 2,
    "Eggs": 1,
    "Rice": 3
}

subtotal = 0

print("🛒 Shopping Bill")
print("------------------------------")
print("Item     Qty   Price   Total")

for item, qty in cart.items():
    price = items[item]
    item_total = price * qty
    subtotal += item_total
    print(item, " ", qty, "   ", price, "    ", item_total)

# discount logic
discount = 0
if subtotal >= 300:
    discount = subtotal * 0.10

# GST
gst = subtotal * 0.05

final_amount = subtotal + gst - discount

print("\nSummary")
print("------------------------------")
print("Subtotal :", subtotal)
print("GST (5%) :", gst)
print("Discount :", discount)
print("Amount to Pay :", final_amount)

