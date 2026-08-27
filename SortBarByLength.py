# Problem: Sort Bars by Length
#
# You are given a list of strings where each string contains only
# the character "I".
#
# Sort the strings from shortest to longest based on their length.
#
# Example:
#
# Input:
# bars = [
#     "IIII",
#     "III",
#     "IIIIII",
#     "IIII",
#     "IIIIIIIII",
#     "II"
# ]
#
# Output:
# [
#     "II",
#     "III",
#     "IIII",
#     "IIII",
#     "IIIIII",
#     "IIIIIIIII"
# ]
#
# Write a function:
#
# def sortBars(bars):
#
# Return the sorted list.
#
# Constraints:
# - The list contains at least one string.
# - Each string contains only the character "I".
# - Do not modify the contents of the strings.

def sortBars(bars):
    bars = bars[:]  # make a copy

    for i in range(len(bars)):
        for j in range(len(bars) - 1 - i):
            if len(bars[j]) > len(bars[j + 1]):
                bars[j], bars[j + 1] = bars[j + 1], bars[j]

    return bars