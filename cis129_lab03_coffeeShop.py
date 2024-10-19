 # Programmer: Ruben Ruiz 
# Description: This program calculates the total cost of coffee and muffins purchased, including tax.
# Changes made in this commit: Initial version with user inputs and formatted receipt.

# Constants for prices and tax rate
PRICE_COFFEE = 5.00
PRICE_MUFFIN = 4.00
TAX_RATE = 0.06

# Get the number of coffees and muffins from the user

num_coffees = int(input("Enter the number of coffees: "))
num_muffins = int(input("Enter the number of muffins: "))

# Calculate the subtotal
subtotal = (num_coffees * PRICE_COFFEE) + (num_muffins * PRICE_MUFFIN)

# Calculate the tax
tax = subtotal * TAX_RATE

# Calculate the total
total = subtotal + tax

# Print the receipt
print("\nRECEIPT")
print(f"Number of coffees: {num_coffees}")
print(f"Number of muffins: {num_muffins}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")


# Thank the user
print("\nThank you for visiting our Coffee Shop! We hope to see you again soon!")



