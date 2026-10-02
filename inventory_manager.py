import os

print("============================================================")
print("INVENTORY MANAGEMENT SYSTEM")
print("============================================================")

# Check inventory.json file exists
if not os.path.exists("inventory.json"):
    print("Error: inventory.json file not found.")
    exit(1)
else:
    print("inventory.json file found.")
    print("Inventory loaded successfully.")


print("----------------- MENU -----------------")
print("1. Display All Products")
print("2. Add a New Product")
print("3. Update Stock of Product")
print("4. Search for a Product")
print("5. Save Inventory")
print("6. Exit")
print("----------------------------------------")


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


# Functions
def get_valid_input():
    failed_attempts = 0

    while True:
        user_input = input("Enter option (1-6): ")


        if user_input == 1:
            # run display_all_products function
            return None
        elif user_input == 2:
            # run add_new_product function
            return None
        elif user_input == 3:
            # run update_stock function
            return None
        elif user_input == 4:
            # run search_product function
            return None
        elif user_input == 5:
            # run save_inventory function
            return None
        elif user_input == 6:
            return "quit", 0, failed_attempts

     

       
        if not user_input.isdigit() or int(user_input) < 0:
            print("Error! Please enter a valid integer.")
            failed_attempts += 1




# Main Program
def main():

    while True:
        return None


