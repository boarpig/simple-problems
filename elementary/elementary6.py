#!/usr/bin/python
#
# Write a program that asks the user for a number n and gives him the
# possibility to choose between computing the sum and computing the product of
# 1,…,n.

def product(n):
    prod = 1
    for i in range(1, number + 1):
        prod *= i
    return prod

print("Give a number: ", end="")
number = int(input())
print("Would you like a sum or product of 1...number")
print("1) sum 2) product")
answer = int(input())
if answer == 1:
    print(sum(range(1, number + 1)))
elif answer == 2:
    print(product(answer))

