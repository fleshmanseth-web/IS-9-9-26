#Assignment 4 by Seth Fleshman
#This program records expenses in a list and tallies out analysis when finished

#Create a list to hold expenses and set the count for each 
expenses = []
small_count = 0
moderate_count = 0
large_count = 0

#Collect expenses until the user enters 0.
while True:
        try:
            expense = float(input("Enter an expense (0 to finish): $"))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if expense < 0:
            print("Please enter a finite, nonnegative amount.")
        elif expense == 0:
            break
        else:
            expenses.append(expense)

#Determines what category each expense is and output that to the user
for expense in expenses:
    if expense < 25:
        classification = "Small expense"
        small_count += 1
    elif expense <= 100:
        classification = "Moderate expense"
        moderate_count += 1
    else:
        classification = "Large expense"
        large_count += 1

#Create and deliver the report
total = sum(expenses)
print("\nExpense summary:")
print(f"Total number of expenses: {len(expenses)}")
print(f"Total expenses: ${total:,.2f}") \

if expenses:
    print(f"Average expense: ${total / len(expenses):,.2f}")
    print(f"Smallest expense: ${min(expenses):,.2f}")
    print(f"Largest expense: ${max(expenses):,.2f}")
else:
    print("Average expense: N/A (no expenses)")
    print("Smallest expense: N/A (no expenses)")
    print("Largest expense: N/A (no expenses)")

print("\n")
print(f"Number of small expenses: {small_count}")
print(f"Number of moderate expenses: {moderate_count}")
print(f"Number of large expenses: {large_count}")