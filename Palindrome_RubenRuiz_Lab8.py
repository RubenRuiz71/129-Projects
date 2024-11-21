
#Module 8: Lab Ruben Ruiz 


def is_palindrome(s):

    # Normalize the string: convert to lowercase and remove spaces and punctuation
    normalized_str = ''.join(char.lower() for char in s if char.isalnum())
    
    # Use a stack (implemented as a list) to store characters
    stack = []
    for char in normalized_str:
        stack.append(char)
    
    # Compare characters from the beginning with popped characters from the stack
    for char in normalized_str:
        if char != stack.pop():
            return False
    
    # If all characters match, it's a palindrome
    return True

# Example usage:
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("race a car"))  # False
print(is_palindrome("radar"))  # True
print(is_palindrome("hanah"))  # True
print(is_palindrome("racecar"))  # True
print(is_palindrome(""))  # True (empty string is considered a palindrome)


# Section 5.11

# Fixing the issue by importing string in the correct scope
from collections import Counter
import string

# Define the function to summarize letters in a string
def summarize_letters(input_string):
    # Clean the string: convert to lowercase, remove spaces and punctuation
    cleaned_string = ''.join(
        char.lower() for char in input_string if char.isalpha()
    )

    # Count frequencies of letters
    letter_counts = Counter(cleaned_string)

    # Convert to a list of tuples (letter, frequency)
    letter_frequency_list = sorted(letter_counts.items())

    return letter_frequency_list

# Function to check if the string contains all letters of the alphabet
def has_all_letters(input_string):
    alphabet = set(string.ascii_lowercase)
    letters_in_string = set(char.lower() for char in input_string if char.isalpha())
    return alphabet.issubset(letters_in_string)

# Test the function
test_string = "The quick brown fox jumps over the lazy dog!"

# Summarize letters and print results
letter_summary = summarize_letters(test_string)
for letter, frequency in letter_summary:
    print(f"'{letter}': {frequency}")

# Check if the string contains all letters of the alphabet
if has_all_letters(test_string):
    print("\nThe string contains all the letters of the alphabet.")
else:
    print("\nThe string does not contain all the letters of the alphabet.")
