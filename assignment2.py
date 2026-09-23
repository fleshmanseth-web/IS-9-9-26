# Road Trip Planner by Seth Fleshman

# This program asks for trip information and 
#   estimates the trip cost summary.

# Print the opening header
print("================================")
print("ROAD TRIP PLANNER")
print("================================")

# Get trip information from the user.
traveler_name = input("What is your name? ")
destination = input("Where are you traveling? ")
one_way_distance = float(input("How many miles is the trip one way? "))
miles_per_gallon = float(input("What is your vehicle's miles per gallon? "))
gas_price = float(input("What is the gas price per gallon? "))
number_of_travelers = int(input("How many travelers are going? "))

# Calculate the total round-trip miles, gas needed, and costs.
total_miles = one_way_distance * 2
gallons_needed = total_miles / miles_per_gallon
estimated_gas_cost = gallons_needed * gas_price
cost_per_traveler = estimated_gas_cost / number_of_travelers

# Display the personalized trip summary.
print("\n================================")
print("TRIP SUMMARY")
print("================================\n")
print(f"Traveler: {traveler_name.upper()}")
print(f"Destination: {destination.upper()}\n")
print(f"Total Miles: {total_miles:.1f}")
    #This :.1f will only work inside an f-string
print(f"Gallons of Gas: {gallons_needed:.1f}")
print(f"Gas Cost: ${estimated_gas_cost:.2f}\n")
print(f"Cost per Traveler: ${cost_per_traveler:.2f}\n")
print("================================\n")
print("Have a great trip!\n")

# AI Disclosure: This program was made in collaboration with ChatGPT 5.5