def display_menu():
    menu = {
        "chicken biryani": 100,
        "mutton biryani": 150,
        "fish biryani": 200,
        "prawns biryani": 250,
        "gulab jamun": 10
    }
    print("\n--- MENU ---")
    for item, price in menu.items():
        print(f"{item.title()} - RS {price}")
    print()
    return menu

def calculate_bill(order_items):
    total = sum(order_items.values())
    print(f"\nYour total bill is: RS {total}")
    return total

def process_payment(total):
    while True:
        payment_mode = input("Please enter mode of payment (cash/online): ").strip().lower()
        if payment_mode == "online":
            print(f"Please send RS {total} to this number: 9398669434")
            break
        elif payment_mode == "cash":
            print("Sorry, cash payments are not accepted. Please choose online payment.")
        else:
            print("Invalid input. Please enter 'cash' or 'online'.")

def take_order(menu):
    order_items = {}
    while True:
        item = input("Enter the item name you want to order (or type 'done' to finish): ").strip().lower()
        if item == 'done':
            break
        elif item in menu:
            while True:
                try:
                    quantity = int(input(f"How many plates/pieces of {item.title()} would you like? "))
                    if quantity > 0:
                        order_items[item] = menu[item] * quantity
                        print(f"{quantity} {item.title()} added to your order.")
                        break
                    else:
                        print("Please enter a valid quantity (greater than 0).")
                except ValueError:
                    print("Invalid input. Please enter a number for quantity.")
        else:
            print("Sorry, that item is not on the menu. Please choose a valid item.")
    return order_items

def main():
    print("WELCOME TO THE LOL AND LOS CAFE")
    customer_name = input("Enter your name: ").strip().title()
    print(f"Hello {customer_name}, what would you like to order today?")
    
    while True:
        dine_type = input("Dine in or Take away: ").strip().lower()
        if dine_type == "take away":
            menu = display_menu()
            wants_menu = input(f"Do you want to see the menu again, {customer_name}? (yes/no): ").strip().lower()
            if wants_menu == "yes":
                display_menu()
            
            order_items = take_order(menu)
            if not order_items:
                print("No items were ordered. Thank you for visiting!")
                break
            
            total_bill = calculate_bill(order_items)
            process_payment(total_bill)
            
            print("\nPlease show your payment transaction details at the takeaway area and collect your order.")
            print(f"Thank you for your order, {customer_name}. Visit again!\n")
            break
        elif dine_type == "dine in":
            print("Sorry, dine-in is not available at the moment. Please select takeaway.\n")
        else:
            print("Invalid option. Please enter 'dine in' or 'take away'.")

if __name__ == "__main__":
    main()
