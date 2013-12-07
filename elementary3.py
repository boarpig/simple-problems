#!/usr/bin/python
#
# Write a program that asks the user for his name and greets him with his name.

print("What is your name? ", end="")
name = input()
if name == 'Alice' or name == 'Bob':
    print("Hello, ", name)
else:
    print("Hello")


