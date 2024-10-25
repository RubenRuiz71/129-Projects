
# CIS129 Ruben Ruiz Lab 5  Part ( 1 , 2 , 3 )
# Date: October 24 , 2024
# Description: This program tracks the total number of bottles returned over seven days,
# calculates the total payout based on a per-bottle rate, and allows the user to repeat the process.




def process_sales():
    # Get the monthly Sales
    monthly_sales = float(input("Enter the monthly sales: "))

    # Get the Increase in Sales
    sales_increase = float(input("Enter the increase in sales: "))

    # Calculate the Store Bonus (example calculation, change as needed)
    store_amount = monthly_sales * 0.1  # Example calculation

    # Calculate the Employee Bonus (example calculation, change as needed)
    emp_amount = sales_increase * 0.05  # Example calculation

    # Print out all the results
    print(f"\nStore Bonus: ${store_amount:.2f}")
    print(f"Employee Bonus: ${emp_amount:.2f}")

def main_while_loop():
    keepGoing = "y"
    
    while keepGoing.lower() == "y":
        process_sales()
        keepGoing = input("Do you want to run the program again? (Enter y for yes): ")

def main_do_while_loop():
    keepGoing = "y"
    
    while True:
        process_sales()
        keepGoing = input("Do you want to run the program again? (Enter y for yes): ")
        
        if keepGoing.lower() != "y":
            break

# Main function to choose loop type
def main():
    loop_type = input("Enter 'while' to use the while loop or 'do-while' to use the do-while loop simulation: ").strip().lower()
    
    if loop_type == "while":
        main_while_loop()
    elif loop_type == "do-while":
        main_do_while_loop()
    else:
        print("Invalid choice. Please enter 'while' or 'do-while'.")

# Run the main function
if __name__ == "__main__":
    main()





#LAB 5 
# PART2






def get_bottles():
    # Constants
    NBR_OF_DAYS = 7
    total_bottles = 0  # Initialize total bottles
    counter = 1        # Initialize counter
    today_bottles = 0  # Initialize bottles for today

    # Loop for each day
    while counter <= NBR_OF_DAYS:
        print(f"Enter number of bottles returned for day {counter}:")
        today_bottles = int(input())  # Get number of bottles for the day
        total_bottles += today_bottles  # Accumulate total bottles
        counter += 1  # Increment counter

    return total_bottles

def calc_payout(total_bottles):
    PAYOUT_PER_BOTTLE = 0.10
    total_payout = total_bottles * PAYOUT_PER_BOTTLE
    return total_payout

def print_info(total_bottles, total_payout):
    print(f"\nTotal number of bottles collected: {total_bottles}")
    print(f"Total payout: ${total_payout:.2f}")

def main():
    keep_going = "y"  # Initialize to allow the loop to run

    while keep_going.lower() == "y":
        total_bottles = get_bottles()  # Get the total bottles for the week
        total_payout = calc_payout(total_bottles)  # Calculate the total payout
        print_info(total_bottles, total_payout)  # Print out the results
        
        print("Do you want to enter another week’s worth of data? (Enter y or n):")
        keep_going = input()  # Ask if the user wants to continue

if __name__ == "__main__":
    main()





# LAB 5 
# PART 3 





def get_bottles():
    """
    Prompts the user to enter the number of bottles returned for each day of the week.
    Returns the total number of bottles collected for the week.
    """
    nbr_of_days = 7
    total_bottles = 0  # Initialize total bottles
    counter = 1        # Initialize counter
    today_bottles = 0  # Initialize bottles for today

    # Loop for each day
    while counter <= nbr_of_days:
        print(f"Enter number of bottles for day #{counter}:")
        today_bottles = int(input())  # Get number of bottles for the day
        total_bottles += today_bottles  # Accumulate total bottles
        counter += 1  # Increment counter

    return total_bottles

def calc_payout(total_bottles):
    """
    Calculates the total payout based on the number of bottles collected.
    Returns the total payout.
    """
    payout_per_bottle = 0.10
    total_payout = total_bottles * payout_per_bottle
    return total_payout

def print_info(total_bottles, total_payout):
    """
    Prints the total number of bottles collected and the total payout.
    """
    print(f"\nThe total number of bottles collected is {total_bottles}")
    print(f"The total paid out is $ {total_payout:.2f}")

def main():
    """
    Main function to run the bottle return program. Allows the user to enter data for multiple weeks.
    """
    keep_going = "y"  # Initialize to allow the loop to run

    while keep_going.lower() == "y":
        # Step 2: Code to set value of variables
        total_bottles = get_bottles()  # Get the total bottles for the week
        total_payout = calc_payout(total_bottles)  # Calculate the total payout
        print_info(total_bottles, total_payout)  # Print out the results
        
        # Ask user if they want to run the program again
        print("\nDo you want to enter another week’s worth of data? (Enter y or n):")
        keep_going = input()  # Get user's choice

if __name__ == "__main__":
    main()
