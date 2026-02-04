class ShoppingCart:
    def __init__(self):
        self.items = {
            "Milk": 50,
            "Bread": 40,
            "Eggs": 120,
            "Rice": 60,
            "Sugar": 45
        }
        self.cart = {}

    def show_items(self):
        print("\nAvailable Items:")
        for item, price in self.items.items():
            print(item, "-", price)

    def add_item(self):
        item = input("Enter item name: ").title()
        if item in self.items:
            qty = int(input("Enter quantity: "))
            if item in self.cart:
                self.cart[item] += qty
            else:
                self.cart[item] = qty
            print(item, "added to cart")
        else:
            print("Item not available")

    def remove_item(self):
        if not self.cart:
            print("\nCart is empty")
            return

        print("\nItems in Cart:")
        for item in self.cart:
            print("-", item)

        item = input("Enter item name to remove: ").title()
        if item in self.cart:
            del self.cart[item]
            print(item, "removed from cart")
        else:
            print("Item not found in cart")

    def view_bill(self):
        if not self.cart:
            print("\nCart is empty")
            return

        subtotal = 0
        print("\nYour Cart:")
        print("Item   Qty   Price   Total")

        for item, qty in self.cart.items():
            price = self.items[item]
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


# -------- MAIN PROGRAM --------
cart = ShoppingCart()

while True:
    print("\n===== MENU =====")
    print("1. Show items")
    print("2. Add item to cart")
    print("3. View cart & bill")
    print("4. Remove item from cart")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        cart.show_items()
    elif choice == "2":
        cart.add_item()
    elif choice == "3":
        cart.view_bill()
    elif choice == "4":
        cart.remove_item()
    elif choice == "5":
        print("Thank you for shopping 😊")
        break
    else:
        print("Invalid choice, try again")
