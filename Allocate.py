#!/usr/bin/python3
#money allocation program
#money allocation program
totalCash = int(input("Enter totalCash: "))
Denomination = [200, 100, 50, 25, 20, 10, 5]
count = 0
for order in range(len(Denomination)):
    print("D{} * ".format(Denomination[order]),end="")
    DenominationValue = int(input())
    totalAmount = Denomination[order] * DenominationValue
    print(totalAmount)
    count += totalAmount
print("Total-Amount is: {}\n".format(count))
if totalCash > count:
    print("You have Surplus of {}".format(count - totalCash))
elif totalCash == count:
    print("Your money is OK {}".format(count))
else:
    print("You have a Shortage of {}".format(count - totalCash))

