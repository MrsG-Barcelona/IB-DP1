"""
===================================================================
IB COMPUTER SCIENCE - THEME B2 LAB ASSIGNMENT
Topic: Control Flow, Loops, and Linear Data Structures
===================================================================
Instructions:
- Implement the function logic for each problem inside the given definition.
- Do NOT use advanced Python data structures like dictionaries ({}), sets, 
  or external libraries.
- Run this file to test your solutions against the provided test cases.
===================================================================
"""


# =================================================================
# PROBLEM 1: Simple Array Sum
# =================================================================
# Description:
# Given an array of integers, find the sum of its elements.
#
# Input: A list of integers `ar`.
# Output: Return the sum of all elements as an integer.
# =================================================================
def simpleArraySum(ar: list[int]) -> int:
    # TODO: Implement your solution here
    pass


# --- Test Cases for Problem 1 ---
print("--- Testing Problem 1: Simple Array Sum ---")
print("Test 1:", "PASS" if simpleArraySum([1, 2, 3, 4, 10, 11]) == 31 else "FAIL")
print("Test 2:", "PASS" if simpleArraySum([5, 10, 15]) == 30 else "FAIL")
print()


# =================================================================
# PROBLEM 2: Compare the Triplets
# =================================================================
# Description:
# Alice and Bob each created a problem for HackerRank. A reviewer
# rates the two challenges, awarding points in three categories:
# clarity, originality, and difficulty.
#
# Given rating lists `a` and `b` (each containing 3 integers):
# - If a[i] > b[i], Alice receives 1 point.
# - If a[i] < b[i], Bob receives 1 point.
# - If a[i] == b[i], neither person receives a point.
#
# Input: Two lists of 3 integers each (`a` and `b`).
# Output: Return a list of 2 integers: [Alice's score, Bob's score].
# =================================================================
def compareTriplets(a: list[int], b: list[int]) -> list[int]:
    # TODO: Implement your solution here
    pass


# --- Test Cases for Problem 2 ---
print("--- Testing Problem 2: Compare the Triplets ---")
print("Test 1:", "PASS" if compareTriplets([5, 6, 7], [3, 6, 10]) == [1, 1] else "FAIL")
print("Test 2:", "PASS" if compareTriplets([17, 28, 30], [99, 16, 8]) == [2, 1] else "FAIL")
print()


# =================================================================
# PROBLEM 3: A Very Big Sum
# =================================================================
# Description:
# Calculate and return the sum of the elements in an array, keeping
# in mind that some of those integers may be very large.
#
# Input: A list of large integers `ar`.
# Output: Return the sum as an integer.
# =================================================================
def aVeryBigSum(ar: list[int]) -> int:
    # TODO: Implement your solution here
    pass


# --- Test Cases for Problem 3 ---
print("--- Testing Problem 3: A Very Big Sum ---")
big_test = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
print("Test 1:", "PASS" if aVeryBigSum(big_test) == 5000000015 else "FAIL")
print()


# =================================================================
# PROBLEM 4: Plus Minus
# =================================================================
# Description:
# Given an array of integers, calculate the ratios of its elements
# that are positive, negative, and zero. Print the decimal value of 
# each fraction on a new line, formatted to 6 decimal places.
#
# Input: A list of integers `arr`.
# Output: Print three floating-point numbers on separate lines:
#         1. Ratio of positive numbers
#         2. Ratio of negative numbers
#         3. Ratio of zero numbers
# =================================================================
def plusMinus(arr: list[int]) -> None:
    # TODO: Implement your solution here (Print output directly)
    pass


# --- Test Cases for Problem 4 ---
print("--- Testing Problem 4: Plus Minus ---")
print("Expected Output:\n0.500000\n0.333333\n0.166667")
print("Actual Output:")
plusMinus([-4, 3, -9, 0, 4, 1])
print()


# =================================================================
# PROBLEM 5: Birthday Cake Candles
# =================================================================
# Description:
# You are in charge of the cake for a child's birthday. You have
# decided the cake will have one candle for each year of their total 
# age. They will only be able to blow out the tallest candles.
# Count how many candles are the maximum height.
#
# Input: A list of integers `candles` representing candle heights.
# Output: Return the count of the tallest candles as an integer.
# =================================================================
def birthdayCakeCandles(candles: list[int]) -> int:
    # TODO: Implement your solution here
    pass


# --- Test Cases for Problem 5 ---
print("--- Testing Problem 5: Birthday Cake Candles ---")
print("Test 1:", "PASS" if birthdayCakeCandles([4, 4, 1, 3]) == 2 else "FAIL")
print("Test 2:", "PASS" if birthdayCakeCandles([3, 2, 1, 3]) == 2 else "FAIL")
print("Test 3:", "PASS" if birthdayCakeCandles([1, 1, 1, 1]) == 4 else "FAIL")
print()


# =================================================================
# PROBLEM 6: Staircase
# =================================================================
# Description:
# Print a staircase of size `n` using `#` symbols and spaces.
# The base and height are both equal to `n`. The last line has no 
# leading spaces, and the first line has `n-1` leading spaces.
#
# Example for n = 4:
#    #
#   ##
#  ###
# ####
#
# Input: An integer `n`.
# Output: Print the staircase directly to the console.
# =================================================================
def staircase(n: int) -> None:
    # TODO: Implement your solution here
    pass


# --- Test Cases for Problem 6 ---
print("--- Testing Problem 6: Staircase (n = 4) ---")
staircase(4)
print()


# =================================================================
# PROBLEM 7: Mini-Max Sum
# =================================================================
# Description:
# Given five positive integers, find the minimum and maximum values 
# that can be calculated by summing exactly four of the five 
# integers. Print the respective minimum and maximum values as a 
# single line of two space-separated integers.
#
# Input: A list of exactly 5 integers `arr`.
# Output: Print `min_sum max_sum` on a single line.
# =================================================================
def miniMaxSum(arr: list[int]) -> None:
    # TODO: Implement your solution here
    pass


# --- Test Cases for Problem 7 ---
print("--- Testing Problem 7: Mini-Max Sum ---")
print("Expected Output: 10 14")
print("Actual Output:  ", end="")
miniMaxSum([1, 2, 3, 4, 5])
print()


# =================================================================
# PROBLEM 8: Diagonal Difference
# =================================================================
# Description:
# Given a square matrix (a 2D list of integers), calculate the 
# absolute difference between the sums of its diagonals.
#
# Primary diagonal:   arr[0][0], arr[1][1], arr[2][2]...
# Secondary diagonal: arr[0][n-1], arr[1][n-2], arr[2][0]...
#
# Input: A square 2D list of integers `arr`.
# Output: Return the absolute diagonal difference as an integer.
# =================================================================
def diagonalDifference(arr: list[list[int]]) -> int:
    # TODO: Implement your solution here
    pass


# --- Test Cases for Problem 8 ---
print("--- Testing Problem 8: Diagonal Difference ---")
matrix_test = [
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12]
]
# Primary = 11 + 5 + (-12) = 4
# Secondary = 4 + 5 + 10 = 19
# Absolute Difference = |4 - 19| = 15
print("Test 1:", "PASS" if diagonalDifference(matrix_test) == 15 else "FAIL")
print()
