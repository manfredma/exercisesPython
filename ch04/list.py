#!/usr/bin/env python3

#列表和元组#

dimensions = (200, 50)
print("Original dimensions: ")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions: ")
for dimension in dimensions:
    print(dimension)


xxx = [1, 2, 3, 4]
yyy = [value**2 for value in xxx]
print(xxx)
print(yyy)