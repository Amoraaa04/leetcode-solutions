# Problem: Contains Duplicates
# Return True if any number appears at least twice in the array

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:   #  nums (List[int]): A list of integers
        # Sort the array first so duplicates are adjacent
        nums.sort()
        # Compare each number with the previous one
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
              #if duplicate is found
                return True
        #if no duplicates are found
        return False
      
# Example usage:
if __name__ == "__main__":
    solution = Solution()

    print(solution.containsDuplicate([1, 2, 3, 1]))  # True
    print(solution.containsDuplicate([1, 2, 3, 4]))  # False
    print(solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))  # True
