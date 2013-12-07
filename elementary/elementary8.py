#!/usr/bin/python
#
# Write a program that prints all prime numbers. (Note: if your programming 
# language does not support arbitrary size numbers, printing all primes up to 
# the largest number you can represent is fine too.)

from math import sqrt, ceil, floor
from time import sleep

def is_prime(n):
    if floor(sqrt(n))**2 == sqrt(n)**2:
        return False
    if n % 2 == 0:
        return False
    for i in range(3, int(ceil(sqrt(n))) + 1, 2):
        if n % i == 0:
            return False
    return True

if __name__=='__main__':
    print(2)
    n = 3
    while 1:
        if is_prime(n):
            print(n)
        n += 1
