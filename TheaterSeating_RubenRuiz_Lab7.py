import math

# Function to add 10 to a number
def add_ten(number):
    """Add 10 to the given number."""
    return number + 10

# Function to determine gender
def gender():
    """Determine if the user is female based on their input."""
    type = input("Enter your gender (male or female): ").strip().lower()
    if type == "male":
        return False
    else:
        return True

# Function to format currency (assuming it’s in USD)
def currency_format(amount):
    """Format the amount as currency."""
    return "${:.2f}".format(amount)

# Function to calculate square root
def calculate_square_root(number):
    """Return the square root of the given number."""
    return math.sqrt(number)

# Main code
if __name__ == "__main__":
    # Example usage of add_ten
    num = int(input("Enter a number to add 10 to: "))
    result = add_ten(num)
    print(f"The result after adding 10 is: {result}")

    # Example usage of gender
    is_female = gender()
    print("The user is female." if is_female else "The user is male.")

    # Example usage of calculate_square_root
    my_number = float(input("Enter a number to find the square root of: "))
    sqrt_result = calculate_square_root(my_number)
    print(f"The square root is: {sqrt_result}")

    # Example usage of currency_format
    subtotal = float(input("Enter the subtotal: "))
    tax = 0.06
    total = subtotal + subtotal * tax
    formatted_total = currency_format(total)
    print(f"The total is {formatted_total}")
