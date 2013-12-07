#!/usr/bin/python
#
# Write a program that prints a multiplication table for numbers up to 12.

for i in range(1, 13):
    for j in range(1, 13):
        print(i*j, end="")
        print("\t", end="")
    print()

