"""
Math Toolkit - Main Program
This file runs the menu and calls functions from the other modules.
"""

import math_add_sub
import math_mul_div
import math_extra

def main():
    print("Welcome to the Math Toolkit!")
    while True:
        print("\nChoose an option:")
        print("1. Add / Subtract")
        print("2. Multiply / Divide")
        print("3. Extra functions")
        print("4. Quit")

        choice = input("Enter choice (1-4): ")

        if choice == "1":
            math_add_sub.run()
        elif choice == "2":
            math_mul_div.run()
        elif choice == "3":
            math_extra.run()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
