# Zuriel Vending Machine Program

# Menu
menu = {
    "41": ("Coke", 2.00),
    "42": ("Takis", 4.00),
    "43": ("Sprite", 2.00),
    "44": ("Arwa", 1.00),
    "45": ("Almarai Milk", 3.00),
    "46": ("Fanta", 2.00),
    "47": ("Pepsi", 2.00),
    
}

# Display the menu 
def display_menu():
    print("\n--- VENDING MACHINE ---")
    print("MENU:")
    for code, (item, price) in menu.items():
        print(f"[Code {code}] {item}: ${price:.2f}")
    print("\nNote: Type 'exit' anytime to cancel.")

# Calculate and dispense change
def dispense_change(amount_due, amount_paid):
    change = round(amount_paid - amount_due, 2)
    if change > 0:
        print(f"Here’s your change: ${change:.2f}. Don’t forget to grab it!")
    elif change == 0:
        print("Perfect payment! No change needed.")
    return change

# Vending machine logic
def vending_machine():
    while True:
        display_menu()

        # Prompt user for their code selection
        user_code = input("\nEnter the code of the item you’d like: ").strip()

        # Exit condition
        if user_code.lower() == 'exit':
            print("Here is your item, Have a fantastic day!")
            break

        # Code Validation
        if user_code not in menu:
            print("Hmm, that code doesn’t match any item. Please try again.")
            continue

        # Get item details
        item_name, item_price = menu[user_code]
        print(f"You’ve chosen {item_name}, which costs ${item_price:.2f}.")

        # Process payment
        try:
            user_payment = float(input("Please insert your payment: $"))
        except ValueError:
            print("Invalid payment input. Let’s try again.")
            continue

        if user_payment < item_price:
            print(f"Insufficient funds! {item_name} costs ${item_price:.2f}, but you only provided ${user_payment:.2f}.")
            print("Transaction canceled. Please try again.")
            continue

        # Dispense item and give change
        print(f"Dispensing your {item_name}... Enjoy!")
        dispense_change(item_price, user_payment)

        # Ask if the user wants another item
        another = input("Would you like to buy another item? (yes/no): ").strip().lower()
        if another != 'yes':
            print("Thank you, Have a good day!")
            break

# Run the vending machine
if __name__ == "__main__":
    vending_machine()
