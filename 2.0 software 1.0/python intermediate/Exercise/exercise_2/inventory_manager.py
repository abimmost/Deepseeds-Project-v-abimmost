# === SMART INVENTORY MANAGER ===
# Review and comment my code which will be studied by a beginner python programmer

inventory = {}

# Function to format currency values
def format_currency(value):
    return f"${value:.2f}"

# Function to add a new item
def add_item():
    name = input("Enter item name: ").title()
    if name in inventory:
        print("Item already exists.")
        return
    try:
        price = float(input("Enter item price: "))
        stock = int(input("Enter item stock: "))
        category = input("Enter item category: ").title()
        inventory[name] = {"price": price, "stock": stock, "category": category}
        print(f"{name} added successfully.")
    except ValueError:
        print("Invalid input. Try again.")

# Function to update stock
def update_stock():
    name = input("Enter item name to update: ").title()
    if name not in inventory:
        print("Item not found.")
        return
    try:
        change = int(input("Enter stock to add/remove (use - for remove): "))
        inventory[name]["stock"] += change
        if inventory[name]["stock"] < 0:
            inventory[name]["stock"] = 0
        print(f"{name} stock updated.")
    except ValueError:
        print("Invalid number.")

# Function to search by category
def search_by_category():
    category = input("Enter category to search: ").title()
    found = False
    print(f"Items in {category}:")
    for name, item in inventory.items():
        if item["category"] == category:
            print(f"• {name} - {format_currency(item['price'])} ({item['stock']} in stock)")
            found = True
    if not found:
        print("No items found in this category.")

# Function to check low stock
def check_low_stock():
    print("\n⚠️ LOW STOCK ALERT:")
    for name, item in inventory.items():
        if item["stock"] <= 5:
            print(f"- {name} ({item['stock']} units remaining)")

# Function to calculate total inventory value
def total_value():
    value = sum(item["price"] * item["stock"] for item in inventory.values())
    print(f"\nCurrent Inventory Value: {format_currency(value)}")

# === MAIN PROGRAM ===
print("=== SMART INVENTORY MANAGER ===")

while True:
    total_value()
    check_low_stock()
    print("\n1. Add New Item\n2. Update Stock\n3. Search by Category\n4. Check Low Stock\n5. Exit\n")
    try:
        choice = int(input("Choose option: "))
        if choice == 1:
            add_item()
        elif choice == 2:
            update_stock()
        elif choice == 3:
            search_by_category()
        elif choice == 4:
            check_low_stock()
        elif choice == 5:
            print("Exiting program.")
            break
        else:
            print("Invalid option.")
    except ValueError:
        print("Enter a valid number.")
