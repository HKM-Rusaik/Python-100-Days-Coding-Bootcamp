print("Welcome to the tip calculator.")
totalBillAmount = input("What was the total bill? ")
tipPercentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
noOfBillOwners = input("How many people to split the bill? ")

totalAmountToPay = int(totalBillAmount) + int(totalBillAmount) * (int(tipPercentage)/100)

amountToEachPersonToPay = int(totalAmountToPay)/ int(noOfBillOwners)

print(f"Each person should pay : ${amountToEachPersonToPay}")

