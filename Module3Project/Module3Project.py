# Ice Cream Shop Application
# Author: Carlos Dominguez
# Date: 01/29/2025

# Store our ice screem shop's menu items
flavors = ["vanilla", "caramel", "mint"]
toppings = ["sprinkles", "nuts", "cherry"]
prices = {"scoop": 2.50, "topping": 0.50}

def display_menu():
    """Shows available flavors and toppings to the customer"""
    print("\n=== Welcome to the Ice Cream Shop! ===")
    print("\nAvailable flavors:")

    # Loop through the flavor list and show each flavor, then
    # we'll loop through the toppings list and display them
    for flavor in flavors:
        print(f" - {flavor}")

    print("\nAvailable Toppings:")
    for topping in toppings:
        print(f"- {topping}")

    # Display the prices
    print("\nPrices")
    print(f"Scoop: ${prices['scoop']:.2f} each")
    print(f"Toppings: ${prices['topping']:.2f} each")


def get_flavors():
    """Gets ice cream flavor choices from the customer"""
    chosen_flavors = []

    # Use a while loop to keep taking orders until the customer is done
    while True:
        try:
            # Prompt the user to choose their scoops of ice cream
            num_scoops = int(input("\nHow many scoops would you like? (1-3)"))
            # Validate the input
            if 1 <= num_scoops <= 3:
                break
            print("Please choose between 1-3 scoops.")
        except ValueError:
            print("Please enter a number.")

    # Prompt the user to enter the ice cream flavor
    print("\nFor each scoop, enter the flavor you'd like:")
    for i in range(num_scoops): #For loop prompts for each scoop of ice cream
        # Nested while loop handles the user's input and validation
        while True:
            flavor = input(f"Scoop {i+1}: ").lower()
            # Check to see if the flavor is one that's in the shop's list
            if flavor in flavors:
                chosen_flavors.append(flavor)
                break
            print("Sorry, that flavor isn't available.")
    
    # Return to the calling function, the number of scoops the user wants
    # and the flavors they picked
    return num_scoops, chosen_flavors

def get_toppings():
    """Gets topping choices from the customer"""
    chosen_toppings = []

    # Use a while loop to prompt the user for the toppings until they 
    # are done adding toppings
    while True:
        topping = input("\nEnter a topping (or 'done' if finished): ").lower()
        #Test if the user is done ordering toppings
        if topping == 'done':
            break
        # Test if the topping is in the list of toppings for our shop
        if topping in toppings:
            chosen_toppings.append(topping)
            print(f"Added {topping}!")
        else:
            print("Sorry, that topping isn't available.")

    # Return the list of toppings that the user chose
    return chosen_toppings

    # Main function - updated test function
def main():
    display_menu()
    # Call get flavors function, which returns the number of scoops
    # and the list of flavors
    num_scoops, chosen_flavors = get_flavors()
    # Call the get toppings functions which returns the list of toppings
    chosen_toppings = get_toppings()
    # Display an order summary
    print("\nOrder Summary:")
    print(f"Scoops: {chosen_flavors}")
    print(f"Toppings: {chosen_toppings}")

    # Automatically execute the main function when the application runs
if __name__ == "__main__":
    main()