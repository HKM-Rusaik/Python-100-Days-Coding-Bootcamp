print("Welcome to the tip calculator.")
try:
    totalBillAmount = input("What was the total bill? ")
    tipPercentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
    if tipPercentage not in [10, 12, 15]:
        raise ValueError("Invalid input. Please enter 10, 12, or 15.")
    noOfBillOwners = input("How many people to split the bill? ")

except ValueError as ve:
    print(ve)
    print("Please enter valid input.")

try:
    totalAmountToPay = int(totalBillAmount) + int(totalBillAmount) * (tipPercentage / 100)

    amountToEachPersonToPay = totalAmountToPay / int(noOfBillOwners)

    print(f"Each person should pay: ${amountToEachPersonToPay:.2f}")

except ZeroDivisionError:
    print("Number of bill owners cannot be zero.")
except ValueError:
    print("Invalid input. Please make sure to enter valid numbers.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
