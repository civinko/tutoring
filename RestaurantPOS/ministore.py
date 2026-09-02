
"""
============================================================
RESTAURANT POS SYSTEM
============================================================

PROJECT GOAL:
Build a scalable Point of Sale (POS) system for a restaurant.

The program should eventually allow restaurant employees to:

- View the restaurant menu
- Create customer orders
- Add items to an order
- Remove items from an order
- Change item quantities
- Add special instructions
- Calculate subtotal, tax, discounts, and total
- Accept payments
- Calculate change
- Print receipts
- Manage multiple tables
- Manage inventory
- Track completed orders
- Save transaction history
- Allow employee logins
- Track sales
- Generate reports


============================================================
PROJECT ROADMAP
============================================================

WEEK 1:
Basic Restaurant Ordering System

- Create restaurant menu
- Display menu
- Create an empty order
- Add items to order
- Remove items
- View order
- Calculate subtotal


WEEK 2:
Checkout System

- Calculate tax
- Add tips
- Accept payment
- Calculate change
- Print receipt
- Validate user input


WEEK 3:
Restaurant Features

- Table numbers
- Multiple active orders
- Dine-in vs takeout
- Special instructions
- Order status
- Modify existing orders


WEEK 4:
Object-Oriented Programming

Convert major parts of the program into classes:

- MenuItem
- OrderItem
- Order
- Table
- Employee
- Restaurant


WEEK 5:
Saving Data

- Save menu to JSON
- Load menu from JSON
- Save transaction history
- Save completed orders
- Store employee accounts


WEEK 6:
Inventory

- Track ingredient/item stock
- Reduce stock after purchases
- Prevent ordering unavailable items
- Restock products
- Low-stock warnings


WEEK 7:
Employee System

- Employee login
- Employee ID
- Manager permissions
- Cashier permissions
- Track employee sales


WEEK 8:
Reporting

- Daily sales
- Number of orders
- Average order value
- Most popular item
- Revenue by menu item
- Revenue by employee


FUTURE FEATURES:

- GUI using Tkinter
- SQLite database
- Credit card payment simulation
- Split checks
- Multiple payment methods
- Refunds
- Coupons
- Loyalty program
- Kitchen display system
- Online ordering
"""


# ============================================================
# CONSTANTS
# ============================================================

# Restaurant sales tax.
TAX_RATE = 0.06

# Restaurant name.
RESTAURANT_NAME = "Python Bistro"


# ============================================================
# MENU
# ============================================================

# The menu is stored as a dictionary.
#
# The key is the item's ID.
#
# Each menu item contains:
# - name
# - category
# - price
# - availability
#
# Later we can move this information into a JSON file
# or database.

menu = {

    "101": {
        "name": "Classic Burger",
        "category": "Entree",
        "price": 10.99,
        "available": True
    },

    "102": {
        "name": "Chicken Sandwich",
        "category": "Entree",
        "price": 9.99,
        "available": True
    },

    "103": {
        "name": "Caesar Salad",
        "category": "Entree",
        "price": 8.99,
        "available": True
    },

    "201": {
        "name": "French Fries",
        "category": "Side",
        "price": 3.99,
        "available": True
    },

    "202": {
        "name": "Onion Rings",
        "category": "Side",
        "price": 4.49,
        "available": True
    },

    "301": {
        "name": "Soda",
        "category": "Drink",
        "price": 2.49,
        "available": True
    },

    "302": {
        "name": "Lemonade",
        "category": "Drink",
        "price": 2.99,
        "available": True
    },

    "401": {
        "name": "Chocolate Cake",
        "category": "Dessert",
        "price": 5.99,
        "available": True
    }
}


# ============================================================
# ACTIVE ORDER
# ============================================================

# For Week 1 we will only support ONE order at a time.
#
# Later we will support:
#
# active_orders = {
#     1: {...},
#     2: {...},
#     3: {...}
# }
#
# This would allow multiple tables/orders to exist at once.


current_order = {

    "order_number": 1,

    "order_type": "dine-in",

    "table_number": None,

    "items": {},

    "special_instructions": "",

    "status": "open"
}


# ============================================================
# DISPLAY MENU
# ============================================================

def display_menu():
    """
    Display all available restaurant menu items.

    REQUIREMENTS:

    1. Loop through the menu dictionary.

    2. Display:
       - Item ID
       - Item name
       - Category
       - Price

    3. Do NOT display unavailable items.

    EXAMPLE:

    ------------------------------------------
    PYTHON BISTRO MENU
    ------------------------------------------

    101 | Classic Burger     | $10.99
    102 | Chicken Sandwich   | $9.99
    201 | French Fries       | $3.99
    """

    # TODO:
    # Student will implement this function.

    pass


# ============================================================
# ADD ITEM
# ============================================================

def add_item(order):
    """
    Add a menu item to an order.

    REQUIREMENTS:

    1. Ask user for an item ID.

    2. Check whether the item exists.

    3. Check whether the item is available.

    4. Ask for quantity.

    5. Quantity must be greater than 0.

    6. Add the item to order["items"].

    Example order:

    {
        "101": {
            "name": "Classic Burger",
            "price": 10.99,
            "quantity": 2
        }
    }

    IMPORTANT:

    If the item already exists in the order,
    increase its quantity instead of creating
    another copy.
    """

    # TODO:
    # Student will implement this function.

    pass


# ============================================================
# REMOVE ITEM
# ============================================================

def remove_item(order):
    """
    Remove an item from the current order.

    REQUIREMENTS:

    1. Display the current order.

    2. Ask which item should be removed.

    3. Verify that the item is actually in the order.

    4. Ask how many should be removed.

    Example:

    Current order:

    Burger x3

    Remove quantity:
    2

    New order:

    Burger x1


    EDGE CASE:

    If the customer removes every item,
    delete the item completely from the order.
    """

    # TODO

    pass


# ============================================================
# VIEW ORDER
# ============================================================

def view_order(order):
    """
    Display everything currently in the order.

    REQUIREMENTS:

    Display:

    - Item name
    - Quantity
    - Price per item
    - Total price for that item

    EXAMPLE:

    ------------------------------------------
    CURRENT ORDER
    ------------------------------------------

    Classic Burger
    $10.99 x 2 = $21.98

    French Fries
    $3.99 x 1 = $3.99

    ------------------------------------------
    Subtotal: $25.97
    """

    # TODO

    pass


# ============================================================
# CALCULATE SUBTOTAL
# ============================================================

def calculate_subtotal(order):
    """
    Calculate the subtotal of the order.

    Formula:

        item price * quantity

    Add the cost of every item together.

    REQUIREMENT:

    This function should RETURN the subtotal.

    Do not only print it.

    Example:

        return 25.97
    """

    # TODO

    return 0


# ============================================================
# CALCULATE TAX
# ============================================================

def calculate_tax(subtotal):
    """
    Calculate sales tax.

    Formula:

        subtotal * TAX_RATE

    REQUIREMENT:

    Return the tax amount.
    """

    # TODO

    return 0


# ============================================================
# CALCULATE TOTAL
# ============================================================

def calculate_total(subtotal, tax):
    """
    Calculate final order total.

    Formula:

        subtotal + tax

    Later this function may also include:

    - discounts
    - coupons
    - service charges
    - tips
    """

    # TODO

    return 0


# ============================================================
# CHECKOUT
# ============================================================

def checkout(order):
    """
    Complete the customer's order.

    REQUIREMENTS:

    1. Make sure the order is not empty.

    2. Calculate subtotal.

    3. Calculate tax.

    4. Calculate total.

    5. Display amount owed.

    6. Ask customer payment amount.

    7. Make sure payment is enough.

    8. Calculate change.

    9. Print receipt.

    10. Mark order status as completed.


    EXAMPLE:

    Subtotal: $25.97
    Tax:       $1.56

    Total:    $27.53

    Payment: $30.00

    Change: $2.47
    """

    # TODO

    pass


# ============================================================
# PRINT RECEIPT
# ============================================================

def print_receipt(order, subtotal, tax, total, payment, change):
    """
    Print a formatted customer receipt.

    EXAMPLE:

    ==========================================
                 PYTHON BISTRO
    ==========================================

    Order #: 1

    Classic Burger
    2 x $10.99                       $21.98

    French Fries
    1 x $3.99                         $3.99

    ------------------------------------------

    Subtotal:                        $25.97
    Tax:                              $1.56

    TOTAL:                           $27.53

    Payment:                         $30.00
    Change:                           $2.47

    ==========================================

                 THANK YOU!

    ==========================================
    """

    # TODO

    pass


# ============================================================
# CLEAR ORDER
# ============================================================

def clear_order(order):
    """
    Clear the current order.

    This could be used if:

    - Customer cancels order
    - Checkout finishes
    - Employee starts a new order

    Be careful:

    We want to clear the ITEMS,
    not destroy the entire order structure.
    """

    order["items"].clear()


# ============================================================
# MAIN POS SCREEN
# ============================================================

def display_pos_options():
    """
    Display the main POS options.

    Example:

    ==========================================
                 PYTHON BISTRO POS
    ==========================================

    1. View Menu
    2. Add Item
    3. Remove Item
    4. View Current Order
    5. Checkout
    6. Cancel Order
    7. Exit

    ==========================================
    """

    print()
    print("=" * 40)
    print(f"{RESTAURANT_NAME} POS")
    print("=" * 40)

    print("1. View Menu")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. View Current Order")
    print("5. Checkout")
    print("6. Cancel Order")
    print("7. Exit")

    print("=" * 40)


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():
    """
    Main POS program.

    The main function controls the application.

    IMPORTANT DESIGN RULE:

    main() should mostly decide WHAT function should run.

    It should NOT contain all of the restaurant logic itself.

    BAD:

        if choice == "2":
            # 40 lines of code for adding an item

    BETTER:

        if choice == "2":
            add_item(current_order)

    Keeping functions separated makes the program easier to:

    - read
    - debug
    - test
    - expand
    """

    while True:

        display_pos_options()

        choice = input("Choose an option: ")

        if choice == "1":

            display_menu()

        elif choice == "2":

            add_item(current_order)

        elif choice == "3":

            remove_item(current_order)

        elif choice == "4":

            view_order(current_order)

        elif choice == "5":

            checkout(current_order)

        elif choice == "6":

            confirm = input(
                "Are you sure you want to cancel this order? (y/n): "
            )

            if confirm.lower() == "y":
                clear_order(current_order)

                print("Order cancelled.")

        elif choice == "7":

            print("Closing POS system...")

            break

        else:

            print("Invalid option. Please try again.")


# ============================================================
# START PROGRAM
# ============================================================

# This prevents main() from automatically running
# if this file is imported into another Python file.
#
# We will discuss why this is useful later in the project.

if __name__ == "__main__":
    main()