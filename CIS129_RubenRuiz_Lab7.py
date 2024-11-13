# Module 7 Lab-7
# Ruben Ruiz
# 11/12/2024





# Constants
SECTION_NAMES = ['A', 'B', 'C']
SEAT_PRICES = {'A': 20, 'B': 15, 'C': 10}
SEAT_CAPACITIES = {'A': 300, 'B': 500, 'C': 200}

def display_constants():
    print("Welcome to the Theater Ticket Sales Program!")
    print(f"Sections: {', '.join(SECTION_NAMES)}")
    for section in SECTION_NAMES:
        print(f"Section {section}: Price ${SEAT_PRICES[section]} per seat, Capacity {SEAT_CAPACITIES[section]} seats")

def get_tickets_sold(section):
    while True:
        try:
            num_tickets = int(input(f"Enter number of tickets sold for Section {section}: "))
            if num_tickets < 0:
                print("Number of tickets cannot be negative. Please try again.")
            elif num_tickets > SEAT_CAPACITIES[section]:
                print(f"Number of tickets exceeds available seats ({SEAT_CAPACITIES[section]}). Please try again.")
            else:
                return num_tickets
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def calculate_income():
    subtotal = 0
    section_totals = {}
    
    for section in SECTION_NAMES:
        tickets_sold = get_tickets_sold(section)
        subtotal += tickets_sold * SEAT_PRICES[section]
        section_totals[section] = tickets_sold
    
        print(f"Subtotal after Section {section}: ${subtotal}")
    
    return subtotal, section_totals

def main():
    display_constants()
    total_income, section_totals = calculate_income()
    
    print("\nSummary:")
    for section in SECTION_NAMES:
        print(f"Section {section}: {section_totals[section]} tickets sold, ${section_totals[section] * SEAT_PRICES[section]}")
    
    print(f"\nTotal income: ${total_income}")

# Entry point
if __name__ == "__main__":
    main()