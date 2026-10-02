import os
import json


INVENTORY_FILE = "inventory.json"


# New Products
product1 = {
    "id": "1004",
    "name": "Keyboard",
    "price": 120.00,
    "stock": 10
}

product2 = {
    "id": "1005",
    "name": "Monitor",
    "price": 300.00,
    "stock": 5
}

product3 = {
    "id": "1006",
    "name": "Webcam",
    "price": 80.00,
    "stock": 15
}

product4 = {
    "id": "1007",
    "name": "Headset",
    "price": 60.00,
    "stock": 20
}

product5 = {
    "id": "1008",
    "name": "External Hard Drive",
    "price": 150.00,
    "stock": 8
}

product_list = [product1, product2, product3, product4, product5]

# =============================
# Functions
# ==============================

# Inventory Functions
# -----------------
def save_inventory(inventory):
    with open(INVENTORY_FILE, "w") as file:
        json.dump(inventory, file, indent=4)

    return True

def load_inventory():
    inventory = []


    # Check inventory.json file exists
    if not os.path.exists(INVENTORY_FILE):
        print("Error: inventory.json file not found.")

        save_inventory(product_list)
        print("A new inventory.json file has been created with default products.")

        return inventory, "Not Found"

    else:
        print("inventory.json file found.")
        print("Inventory loaded successfully.")

        with open(INVENTORY_FILE, "r") as file:
                inventory = json.load(file)
                status = True

                return inventory, "Inventory loaded"


# Data Functions
# -----------------
def search_functions(inventory, product_id):
    for product in inventory:
        if product["id"] == product_id:
            return product
    return None



def add_product(inventory, product_id, name, price, stock):
    if search_functions(inventory, product_id) is not None:
        return False

    product = {
        "id": product_id,
        "name": name,
        "price": price,
        "stock": stock,
    }
    inventory.append(product)
    return True



def update_stock(inventory, product_id, new_stock):
    product = search_functions(inventory, product_id)
    if product is None:
        return False

    product["stock"] = new_stock
    return True

# Display Functions
# -----------------
def display_all(inventory):
    if not inventory:
        print("Inventory is empty.")
        return

    print("\nCurrent Inventory:")
    for product in inventory:
        print(f"ID: {product['id']}, Name: {product['name']}, Price: ${product['price']:.2f}, Stock: {product['stock']}")


def show_menu():
    print("\n----------------- MENU -----------------")
    print("1. Display All Products")
    print("2. Add a New Product")
    print("3. Update Stock of Product")
    print("4. Search for a Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------------------")


# Create/Update/Search UI Display
def add_product_input(inventory):
    product_id = input("Enter Product ID: ")
    name = input("Enter Product Name: ")
    price = float(input("Enter Product Price: "))
    stock = int(input("Enter Product Stock: "))

    if add_product(inventory, product_id, name, price, stock):
        print(f"\nProduct {name} added successfully.")
    else:
        print(f"\nProduct with ID {product_id} already exists.")


def update_stock_input(inventory):
    product_id = input("Enter Product ID to update stock: ")
    new_stock = int(input("Enter New Stock Quantity: "))

    if update_stock(inventory, product_id, new_stock):
        print(f"\nStock for Product ID {product_id} updated successfully.")
    else:
        print(f"\nProduct with ID {product_id} not found.")

def search_product_input(inventory):
    product_id = input("Enter Product ID to search: ")
    product = search_functions(inventory, product_id)

    if product:
        print(f"\nProduct Found: ID: {product['id']}, Name: {product['name']}, Price: ${product['price']:.2f}, Stock: {product['stock']}")
    else:
        print(f"\nProduct with ID {product_id} not found.")


# Save Inventory UI Display
def save_inventory_ui(inventory):
    print("Saving inventory to file...")
    if save_inventory(inventory):
            print(f"Inventory saved successfully to {INVENTORY_FILE}.")
    else:
        print("Error: could not save inventory.")
# ==============================
# Main Program
# =============================
def main():

    print("============================================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("============================================================\n\n")

    inventory, status = load_inventory()

    if status=="loaded":
        print(f"{INVENTORY_FILE} found.")
        print("Inventory loaded successfully.")
    elif status=="Not Found":
        print(f"{INVENTORY_FILE} not found.")
        print("A new inventory.json file has been created with default products.")
    

    if not inventory:
        for p in product_list:
            add_product(inventory, p["id"], p["name"], p["price"], p["stock"])

    exit_program = False

    while not exit_program:
        show_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            display_all(inventory)
        elif choice == "2":
            add_product_input(inventory)
        elif choice == "3":
            update_stock_input(inventory)
        elif choice == "4":
            search_product_input(inventory)
        elif choice == "5":
            save_inventory_ui(inventory)
        elif choice == "6":
            print("Saving inventory before exit...")
            if save_inventory(inventory):
                print("Inventory saved successfully.")
            else:
                print("Error: could not save inventory.")
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            exit_program = True
        else:
            print("Invalid choice. Please try again.")


        
        

if __name__ == "__main__":
    main()

