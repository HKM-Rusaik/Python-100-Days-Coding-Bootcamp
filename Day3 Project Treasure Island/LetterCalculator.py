firstUserName = input("Enter your name : ")
secondUserName = input("Enter your name :")

combinedName = firstUserName + secondUserName

combinedNameInLowerCase = combinedName.replace(" ", "").lower()


# Method 1
t = combinedNameInLowerCase.count("t")
r = combinedNameInLowerCase.count("r")
u = combinedNameInLowerCase.count("u")
e = combinedNameInLowerCase.count("e")
firstDigit = t + r + u + e

l = combinedNameInLowerCase.count("l")
o = combinedNameInLowerCase.count("o")
v = combinedNameInLowerCase.count("V")
e = combinedNameInLowerCase.count("e")
secondDigit = l + o + v + e

totalScore = str(str(firstDigit) + str(secondDigit))
print("Your score is : " + totalScore)

# method 2
total_count1 = str(sum(combinedNameInLowerCase.count(letter) for letter in "true"))
total_count2 = (sum(combinedNameInLowerCase.count(letter) for letter in "love"))
print("Your score is : " + total_count1 + total_count2)
