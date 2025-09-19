# There are two kinds of hot dogs sold:  
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).  
# Also tax is 7%. 
# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost. 

def hotdog_order():
    HOT_DOG_PRICE = 3.50
    CHILI_DOG_PRICE = 4.50
    CHEESE_PRICE = 0.50
    PEPPERS_PRICE = 0.75
    ONIONS_PRICE = 1.00
    TAX_RATE = 0.07

    print("Menu:")
    print("1. Hot Dog ($3.50)")
    print("2. Chili Dog ($4.50)")
    choice = input("Enter 1 for Hot Dog or 2 for Chili Dog: ")

    if choice == "1":
        subtotal = HOT_DOG_PRICE
    elif choice == "2":
        subtotal = CHILI_DOG_PRICE
    else:
        print("Invalid choice.")
        return

    
    cheese = input("Do you want cheese ($0.50)? : ")
    if cheese.lower() == "y":
        subtotal += CHEESE_PRICE

    peppers = input("Do you want peppers ($0.75)? : ")
    if peppers.lower() == "y":
        subtotal += PEPPERS_PRICE

    onions = input("Do you want grilled onions ($1.00)? : ")
    if onions.lower() == "y":
        subtotal += ONIONS_PRICE

    
    tax = subtotal * TAX_RATE
    total = subtotal + tax

    print(f"\nSubtotal: ${subtotal:.2f}")
    print(f"Tax (7%): ${tax:.2f}")
    print(f"Total:    ${total:.2f}")

if __name__ == "__main__":
    hotdog_order()

