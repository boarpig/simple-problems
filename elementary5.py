#!/usr/bin/python

print("Give a number: ", end="")
number = int(input())
print(sum(x for x in range(1, number + 1) if x % 3 == 0 or x % 5 == 0))

