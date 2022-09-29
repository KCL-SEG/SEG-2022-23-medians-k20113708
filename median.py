"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

numbers.sort()

if numbers:
    length = len(numbers)
    if length % 2 == 1:
        print(numbers[length // 2])
    else:
        print((numbers[length // 2] + numbers[(length // 2) - 1]) / 2)
