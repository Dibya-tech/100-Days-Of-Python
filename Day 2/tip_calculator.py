# Asks the user to enter the total bill amount, tip percentage and
# the number of users to split this among. Then it generates individual payment amount

print("Welcome to the tip calculator")
bill_amt = float(input("What was the total bill amount?\n"))
tip_percentage = float(input("What percentage tip would you like to give?\n(Be generous)\n"))
people = int(input("How many of you are splitting the bill?\n"))

individual_amt = (bill_amt + (tip_percentage * bill_amt) / 100) / people
print("Each of you hast to pay " + str(round(individual_amt,2)) + " rupees.")
print("Thank you for using the Tip Calculator. The application will exit now")