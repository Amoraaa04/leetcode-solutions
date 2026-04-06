#Brute force approach

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
      intersection = []     

      for num in nums1:
         if num in nums2 and num not in intersection: # each value in intersection must be unique
            intersection.append(num)

      return intersection

#Optimised approach

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set(nums1)
        intersection = set()

        for num in nums2:
            if num in seen:
                result.add(num)

        return list(intersection)
