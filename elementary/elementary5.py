#!/usr/bin/python
#
# Modify the previous program such that only multiples of three or five are
# considered in the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17

print("Give a number: ", end="")
number = int(input())
print(sum(x for x in range(1, number + 1) if x % 3 == 0 or x % 5 == 0))

