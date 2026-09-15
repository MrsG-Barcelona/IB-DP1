"""
===================================================================
IB COMPUTER SCIENCE (THEME B2) - EXTENSION LAB ASSIGNMENT
Topic: Advanced Array Traversal, Multi-Pointer Logic & Algorithmic Optimization
===================================================================
Instructions:
- Implement the function logic for each problem inside the given definition.
- Constraints: 
    - Do NOT use Theme B4 Abstract Data Types (dicts/hash maps, sets).
    - Do NOT use built-in search/sort helpers like `.index()`, `.count()`, or `sorted()`.
    - Focus on low-level index manipulation, two pointers, and mathematical logic.
- Run this file to verify your solutions against the test cases.
===================================================================
"""


# =================================================================
# PROBLEM 1: Target Finder in a Sorted Array
# =================================================================
# Description:
# Given an array of integers SORTED in ascending order and a target
# value, return the indices of the two numbers that add up to the target.
#
# Constraint: Solve this in a single pass (O(N) time) using two pointers
# (one starting at the left, one at the right) without using nested loops!
#
# Input: A sorted list of integers `arr`, and an integer `target`.
# Output: Return a list of two indices [index1, index2]. If no match, return [].
# =================================================================
def target_finder(arr: list[int], target: int) -> list[int]:
    # TODO: Implement your two-pointer solution here
    pass


# --- Test Cases for Problem 1 ---
print("--- Testing Problem 1: Target Finder in a Sorted Array ---")
print("Test 1:", "PASS" if target_finder([2, 7, 11, 15], 9) == [0, 1] else "FAIL")
print("Test 2:", "PASS" if target_finder([1, 3, 4, 6, 8, 10], 11) == [1, 4] else "FAIL")
print("Test 3:", "PASS" if target_finder([1, 2, 3], 7) == [] else "FAIL")
print()


# =================================================================
# PROBLEM 2: Run-Length Encoding (Basic Compression)
# =================================================================
# Description:
# Given a string of repeated consecutive characters, compress it by 
# replacing consecutive duplicate characters with the character followed 
# by its count.
#
# Example: "AAABBCDDDD" -> "A3B2C1D4"
#
# Input: A non-empty string `s`.
# Output: Return the compressed string.
# =================================================================
def compress_string(s: str) -> str:
    # TODO: Implement your solution here
    pass


# --- Test Cases for Problem 2 ---
print("--- Testing Problem 2: Run-Length Encoding ---")
print("Test 1:", "PASS" if compress_string("AAABBCDDDD") == "A3B2C1D4" else "FAIL")
print("Test 2:", "PASS" if compress_string("A") == "A1" else "FAIL")
print("Test 3:", "PASS" if compress_string("WWWWWWWWWWWWBWWWWWWWWWWWWBBB") == "W12B1W12B3" else "FAIL")
print()


# =================================================================
# PROBLEM 3: In-Place Duplicate Removal from Sorted Array
# =================================================================
# Description:
# Given a sorted list of integers, remove the duplicates IN-PLACE 
# such that each unique element appears only once at the front of the list.
# Return the length of the unique portion of the array.
#
# Constraint: Do NOT create a new list or use `set()`. Modify `arr` directly.
#
# Input: A sorted list of integers `arr`.
# Output: Return an integer representing the new length of unique elements.
# =================================================================
def remove_duplicates(arr: list[int]) -> int:
    # TODO: Implement your solution here
    pass


# --- Test Cases for Problem 3 ---
print("--- Testing Problem 3: In-Place Duplicate Removal ---")
t3_arr1 = [1, 1, 2]
t3_len1 = remove_duplicates(t3_arr1)
print("Test 1:", "PASS" if t3_len1 == 2 and t3_arr1[:t3_len1] == [1, 2] else "FAIL")

t3_arr2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
t3_len2 = remove_duplicates(t3_arr2)
print("Test 2:", "PASS" if t3_len2 == 5 and t3_arr2[:t3_len2] == [0, 1, 2, 3, 4] else "FAIL")
print()


# =================================================================
# PROBLEM 4: Rotate an Array by K Steps
# =================================================================
# Description:
# Rotate an array to the right by `k` steps.
# Example: [1, 2, 3, 4, 5] rotated by k = 2 steps becomes [4, 5, 1, 2, 3].
#
# Hint: Use modulo arithmetic `%` to handle index wraparound if `k` is 
# larger than the length of the array!
#
# Input: A list of integers `nums`, and an integer `k`.
# Output: Return a new list shifted right by `k` positions.
# =================================================================
def rotate_array(nums: list[int], k: int) -> list[int]:
    # TODO: Implement your solution here
    pass


# --- Test Cases for Problem 4 ---
print("--- Testing Problem 4: Rotate an Array by K Steps ---")
print("Test 1:", "PASS" if rotate_array([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4] else "FAIL")
print("Test 2:", "PASS" if rotate_array([-1, -100, 3, 99], 2) == [3, 99, -1, -100] else "FAIL")
print("Test 3:", "PASS" if rotate_array([1, 2], 5) == [2, 1] else "FAIL")
print()


# =================================================================
# PROBLEM 5: Find Peak Element
# =================================================================
# Description:
# An element in an array is a "peak" if it is strictly greater than 
# its adjacent neighbors. Given an array, return the index of ANY one peak.
#
# Boundary rule: Elements at the very beginning (index 0) or very end (index N-1) 
# only need to be greater than their single adjacent neighbor.
#
# Input: A list of integers `nums`.
# Output: Return the index of a peak element as an integer.
# =================================================================
def find_peak_element(nums: list[int]) -> int:
    # TODO: Implement your solution here
    pass


# --- Test Cases for Problem 5 ---
print("--- Testing Problem 5: Find Peak Element ---")
print("Test 1:", "PASS" if find_peak_element([1, 2, 3, 1]) == 2 else "FAIL")
print("Test 2:", "PASS" if find_peak_element([1, 2, 1, 3, 5, 6, 4]) in [1, 5] else "FAIL")
print("Test 3:", "PASS" if find_peak_element([5, 4, 3, 2, 1]) == 0 else "FAIL")
print()


# =================================================================
# PROBLEM 6: Numeric Palindrome Check
# =================================================================
# Description:
# Determine if an integer `x` is a palindrome (reads the same forward 
# and backward).
#
# Strict Rule: You CANNOT convert the integer to a string (no `str(x)`).
# Use modulo `%` to extract digits and floor division `//` to reduce `x`.
# Note: Negative numbers are NOT palindromes (e.g., -121 -> 121-).
#
# Input: An integer `x`.
# Output: Return True if `x` is a palindrome, otherwise False.
# =================================================================
def is_palindrome_numeric(x: int) -> bool:
    # TODO: Implement your mathematical solution here
    pass


# --- Test Cases for Problem 6 ---
print("--- Testing Problem 6: Numeric Palindrome Check ---")
print("Test 1:", "PASS" if is_palindrome_numeric(121) == True else "FAIL")
print("Test 2:", "PASS" if is_palindrome_numeric(-121) == False else "FAIL")
print("Test 3:", "PASS" if is_palindrome_numeric(10) == False else "FAIL")
print("Test 4:", "PASS" if is_palindrome_numeric(12321) == True else "FAIL")
print()


# =================================================================
# PROBLEM 7: Container With Most Water
# =================================================================
# Description:
# Given an array representing vertical line heights, find two lines that 
# together with the x-axis form a container that holds the most water.
#
# Water volume = width * min(height[left], height[right])
#
# Constraint: Solve this in O(N) time using two pointers without nested loops.
#
# Input: A list of positive integers `height`.
# Output: Return the maximum calculated area as an integer.
# =================================================================
def max_area(height: list[int]) -> int:
    # TODO: Implement your solution here
    pass


# --- Test Cases for Problem 7 ---
print("--- Testing Problem 7: Container With Most Water ---")
print("Test 1:", "PASS" if max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49 else "FAIL")
print("Test 2:", "PASS" if max_area([1, 1]) == 1 else "FAIL")
print("Test 3:", "PASS" if max_area([4, 3, 2, 1, 4]) == 16 else "FAIL")
print()


# =================================================================
# PROBLEM 8: Maximum Subarray Sum (Kadane's Algorithm)
# =================================================================
# Description:
# Given an array containing both positive and negative integers, 
# find the contiguous subarray (containing at least one number) 
# which has the largest sum, and return that sum.
#
# Example: [-2, 1, -3, 4, -1, 2, 1, -5, 4] -> Subarray [4, -1, 2, 1] has max sum = 6.
#
# Input: A list of integers `nums`.
# Output: Return the maximum subarray sum as an integer.
# =================================================================
def max_subarray(nums: list[int]) -> int:
    # TODO: Implement your solution here
    pass


# --- Test Cases for Problem 8 ---
print("--- Testing Problem 8: Maximum Subarray Sum ---")
print("Test 1:", "PASS" if max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6 else "FAIL")
print("Test 2:", "PASS" if max_subarray([1]) == 1 else "FAIL")
print("Test 3:", "PASS" if max_subarray([5, 4, -1, 7, 8]) == 23 else "FAIL")
print()