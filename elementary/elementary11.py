#!/usr/bin/python
#
# Write a program that computes 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11...)

sum = 0
for k in range(1, 10**6 + 1):
    sum += ((-1)**(k + 1)) / (2 * k - 1)
print(4 * sum)
