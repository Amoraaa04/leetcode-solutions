class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dictionary = {} # Hash map to store frequency of elements in the smaller list
        intersection = []  #numbers that intersect will be appended here

      # the smaller list will be used for the HashMap to optimise space
        if len(nums1) > len(nums2):
            smaller = nums2   
            larger = nums1
        else:
            smaller = nums1
            larger = nums2

      # Count how many times each number appears in the smaller list
        for num in smaller:  
            if num in dictionary:
                dictionary[num] += 1  # increment by 1 if already in dictionary
            else:
                dictionary[num] = 1  # Initialise count to 1 if not in dictionary
       
      # Iterate through the larger list and check for matches
        for num in larger:
          # If number exists in dictionary and count is still available
            if num in dictionary and dictionary[num] > 0:  
                intersection.append(num) # append to intersection
                dictionary[num] -= 1 # Decrease value to avoid reuse
        return intersection
