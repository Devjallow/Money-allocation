#!/usr/bin/python3
#money allocation program
Denomination = [200, 100, 50, 25, 20, 10, 5]
count = 0
for order in Denomination:
    print("D{} * ".format(order),end="")
    DenominationValue = int(input())
    count += DenominationValue
print(count)
