#!/usr/bin/python
#
# Write a program that prints the next 20 leap years.

from datetime import date
from calendar import isleap

now = date.today()
now = now.year
n = 0

while n < 20:
    if isleap(now):
        n += 1
        print(now)
    now += 1
