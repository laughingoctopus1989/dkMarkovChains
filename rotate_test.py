#!/usr/bin/env python3
#testing order swap function
number = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(number)
print("rotate forward!")
number[0], number[1], number[2] = number[1], number[2], number[0]
print(number)
#still need to setup rotate back!
