# Plus One
# This Python function increments a number represented as a list of digits.

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



