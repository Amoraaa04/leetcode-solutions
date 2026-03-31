# Plus One
# This Python function increments a number represented as a list of digits.
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
          # Start from the least significant digit and move left
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9: 
            #checks if leftmost digit is < 9
                digits[i] += 1
            #if digit is < 9, 1 is added and then returned
                return digits
            else:
                digits[i] = 0
            # If digit is 9, it becomes 0 and  moves to the next left digit
        return [1] + digits


if __name__ == "__main__":
    # Create an instance of the class
    solution = Solution()

    # Example test cases
    print(solution.plusOne([1, 2, 3]))     # Output: [1, 2, 4]
    print(solution.plusOne([4, 3, 2, 1]))  # Output: [4, 3, 2, 2]
    print(solution.plusOne([9]))           # Output: [1, 0]
    print(solution.plusOne([1, 2, 9]))     # Output: [1, 3, 0]
    print(solution.plusOne([9, 9, 9]))     # Output: [1, 0, 0, 0]
