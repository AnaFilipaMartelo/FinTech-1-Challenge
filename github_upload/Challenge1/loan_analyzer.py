# coding: utf-8
import csv
from pathlib import Path

"""
Part 1: Automate the Calculations.

"""
loan_costs = [500, 600, 200, 1000, 450]

# Use the `len` function to calculate the total number of loans in the list.
total_number_loans = len(loan_costs)
# Print the total number of loans
print(f"The total number of loans is: {total_number_loans}.")

# Calculate the total of all loans in the list, using the `sum` function.
total_value_loans= sum(loan_costs)
# Print the total value of the loans
print(f"The total value of the loans is ${total_value_loans}.")

# Calculate the average loan price, using the sum of all loans and the total number of loans.
average_loan_amount = total_value_loans / total_number_loans
# Print the average loan amount
print(f"The average loan amount is ${average_loan_amount}.")

"""
Part 2: Analyze Loan Data.
"""

# Loan data
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Use get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
future_value= loan.get("future_value")
remaining_months= loan.get("remaining_months")
# Print 'future_value' and 'remaining_months' variables.
print(f"The future value of the loan is ${future_value}.")
print(f"The remaining months are {remaining_months}.")

# Calculate present value using a minimum required return of 20% as the discount rate.
present_value= future_value / (1+ 0.20/12)**remaining_months

# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# If the present value of a loan represents its fair value, assuming a required minimum return of 20%, then 
# buying the loan at its current cost depends on whether the current cost is below or above the fair value.
# If the current cost is below the fair value, then buying the loan would likely make sense, as it would 
# represent a potential profit opportunity. However, if the current cost is above the fair value, then buying 
# the loan would not make sense, as it would represent a potential loss.

# Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#   If the present value of the loan is greater than or equal to the cost, then print a message that says the loan 
# is worth at least the cost to buy it.
#   Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is 
# too expensive and not worth the price.
if present_value >= loan.get("loan_price"):
    print("The loan is worth at least the cost of it.")
else:
    print("The loan is too expensive and not worth the price.")


"""
Part 3: Perform Financial Calculations.
"""

# Loan data
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Define a new function that will be used to calculate present value.
# The function has the parameters `future_value`, `remaining_months`, and `annual_discount_rate`
# The function returns the `present_value` for the loan.
def calculate_present_value(future_value, remaining_months, annual_discount_rate):
    present_value= future_value / (1+ annual_discount_rate/12)**remaining_months
    return present_value

# Set `annual_discount_rate` to 0.2 for this new loan calculation.
annual_discount_rate=0.2
# Calculate the present value of the new loan and assign it to 'present_value'.
present_value= calculate_present_value(new_loan["future_value"], new_loan["remaining_months"], annual_discount_rate)
# Print the present value of the loan
print(f"The present value of the loan is: {present_value}")

"""
Part 4: Conditionally filter lists of loans.
"""

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# Create an empty list called `inexpensive_loans`
inexpensive_loans=[]

# Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
for loan in loans:
    if loan["loan_price"] <= 500:
        inexpensive_loans.append(loan)

# Print `inexpensive_loans` list
print(inexpensive_loans)

"""
Part 5: Save the results.
"""

# output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# output file path
output_path = Path("inexpensive_loans.csv")

# Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
with open(output_path, 'w', newline='') as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(header) # write the header variable as the first row
    for loan in inexpensive_loans: # for loop to iterate through each loan in `inexpensive_loans`
        csvwriter.writerow(loan.values())
