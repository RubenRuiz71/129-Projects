# Module 6 Lab-6
# Ruben Ruiz
# 11/05/2024






def getTotalHotDogs():
    attendees = int(input("Enter the number of people attending the cookout: "))
    hotDogsPerPerson = int(input("Enter the number of hot dogs each person will get: "))
    totalHotDogs = attendees * hotDogsPerPerson
    return totalHotDogs

def showResults(total):
    DOGS = 10  # Number of hot dogs per package
    BUNS = 8   # Number of buns per package
    
    dogsLeft = (DOGS - total % DOGS) % DOGS
    minDogs = (total // DOGS) + (0 if dogsLeft == 0 else 1)
    
    bunsLeft = (BUNS - total % BUNS) % BUNS
    minBuns = (total // BUNS) + (0 if bunsLeft == 0 else 1)
    
    print(f"Minimum packages of hot dogs needed: {minDogs}")
    print(f"Minimum packages of hot dog buns needed: {minBuns}")
    print(f"Hot dogs remaining: {dogsLeft}")
    print(f"Hot dog buns remaining: {bunsLeft}")

def main():
    totalHotDogs = getTotalHotDogs()
    showResults(totalHotDogs)

# Entry point
if __name__ == "__main__":
    main()
