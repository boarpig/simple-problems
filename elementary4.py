#!/usr/bin/python
#
# Write a program that asks the user for a number n and prints the sum of the
# numbers 1 to n

print("Give a number: ", end="")
number = int(input())
print(sum(range(1, number + 1)))

