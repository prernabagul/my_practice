items = {
    "Milk": 50,
    "Bread": 40,
    "Eggs": 120,
    "Rice": 60,
    "Sugar": 45
}

cart = {}

while True:
    print("\n===== MENU =====")
    print("1. Show items")
    print("2. Add item to cart")
    print("3. View cart & bill")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    # Show items
    if choice == "1":
        print("\nAvailable Items:")
        for item, price in items.items():
            print(item, "-", price)

    # Add to cart
    elif choice == "2":
        item = input("Enter item name: ").title()
        if item in items:
            qty = int(input("Enter quantity: "))
            if item in cart:
                cart[item] += qty
            else:
                cart[item] = qty
            print(item, "added to cart")
        else:
            print("Item not available")

    # View cart & bill
    elif choice == "3":
        if not cart:
            print("\nCart is empty")
        else:
            subtotal = 0
            print("\nYour Cart:")
            print("Item   Qty   Price   Total")

            for item, qty in cart.items():
                price = items[item]
                total = price * qty
                subtotal += total
                print(item, qty, price, total)

            discount = 0
            if subtotal >= 300:
                discount = subtotal * 0.10

            gst = subtotal * 0.05
            final_amount = subtotal + gst - discount

            print("\nSubtotal:", subtotal)
            print("GST (5%):", gst)
            print("Discount:", discount)
            print("Amount to Pay:", final_amount)

    # Exit
    elif choice == "4":
        print("Thank you for shopping 😊")
        break

    else:
        print("Invalid choice, please try again")
