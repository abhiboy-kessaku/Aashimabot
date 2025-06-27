import numpy as np

class Restaurant:
    def __init__(self):
        # Menu stored as {item_name: (price, category)}
        self.menu = {
            "Pizza": (150, "Main Course"),
            "Burger": (100, "Fast Food"),
            "Coke": (40, "Beverage"),
            "Fries": (60, "Snacks"),
            "IceCream": (80, "Dessert")
        }
        self.orders = []  # List of orders, each order is a list of (item_name, quantity)
        self.total_sales = []

    def show_menu(self):
        print("\n--- MENU ---")
        for item, (price, category) in self.menu.items():
            print(f"{item} - ₹{price} ({category})")

    def add_item_to_menu(self):
        item = input("Enter new item name: ").capitalize()
        if item in self.menu:
            print("Item already exists.")
            return
        try:
            price = float(input("Enter price: ₹"))
            category = input("Enter category (e.g., Beverage, Main Course): ")
            self.menu[item] = (price, category)
            print(f"{item} added successfully!")
        except ValueError:
            print("Invalid price.")

    def take_order(self):
        order = []
        while True:
            self.show_menu()
            item = input("Enter item to order (or 'done' to finish): ").capitalize()
            if item.lower() == 'done':
                break
            if item in self.menu:
                try:
                    qty = int(input(f"Enter quantity for {item}: "))
                    order.append((item, qty))
                except ValueError:
                    print("Invalid quantity.")
            else:
                print("Item not found.")
        if order:
            self.orders.append(order)
            print("Order placed successfully!")

    def generate_bill(self):
        if not self.orders:
            print("No orders yet.")
            return
        last_order = self.orders[-1]
        print("\n--- BILL ---")
        total = []
        for item, qty in last_order:
            price = self.menu[item][0]
            amount = price * qty
            total.append(amount)
            print(f"{item} x {qty} = ₹{amount}")
        bill_total = np.sum(total)
        self.total_sales.append(bill_total)
        print(f"Total Bill: ₹{bill_total:.2f}")

    def show_total_sales(self):
        if not self.total_sales:
            print("No sales yet.")
        else:
            print(f"\nTotal Orders: {len(self.orders)}")
            print(f"Total Sales: ₹{np.sum(self.total_sales):.2f}")
            print(f"Average Sale: ₹{np.mean(self.total_sales):.2f}")
            print(f"Highest Bill: ₹{np.max(self.total_sales):.2f}")
            print(f"Lowest Bill: ₹{np.min(self.total_sales):.2f}")

def main():
    r = Restaurant()
    while True:
        print("\n--- Restaurant Management System ---")
        print("1. Show Menu")
        print("2. Add Item to Menu")
        print("3. Take Order")
        print("4. Generate Bill")
        print("5. Show Total Sales Stats")
        print("6. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            r.show_menu()
        elif choice == "2":
            r.add_item_to_menu()
        elif choice == "3":
            r.take_order()
        elif choice == "4":
            r.generate_bill()
        elif choice == "5":
            r.show_total_sales()
        elif choice == "6":
            print("Thank you for using Restaurant Management System!")
            break
        else:
            print("Invalid Value.Try Again")

if __name__ == "__main__":
    main()
