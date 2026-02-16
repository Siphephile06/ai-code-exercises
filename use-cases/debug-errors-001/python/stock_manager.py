"""
Stock Manager Module

This module provides functionality for managing and reporting on inventory items.
It allows users to display formatted inventory reports to the console.
"""
def print_inventory_report(items):
    """
    Prints a formatted inventory report to the console.
    
    Displays all items in inventory with their names and quantities in a 
    nicely formatted table with header and footer border.
    """
    print("===== INVENTORY REPORT =====")
    # loop through the items
    for i in range(len(items)):
        print(f"Item {i}: {items[i]['name']} - Quantity: {items[i]['quantity']}")
    print("============================")

def main():
    items = [
        {"name": "Laptop", "quantity": 15},
        {"name": "Mouse", "quantity": 30},
        {"name": "Keyboard", "quantity": 25}
    ]
    print_inventory_report(items)

if __name__ == "__main__":
    main()
