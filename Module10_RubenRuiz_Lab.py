# Get the dollar amount from the user
amount = input("Enter the dollar amount: ")

# Format the amount in check-protected format with leading asterisks
# The total width is 10 characters, and the amount is right-aligned with leading '*'
protected_amount = f"{amount:*>10}"

# Print the protected amount
print(protected_amount)
