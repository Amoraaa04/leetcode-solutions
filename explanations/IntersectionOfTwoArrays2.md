# Intersection of Two Arrays II

**Problem Summary**: Given two integer arrays nums1 and nums2, return an array of the values that intersect

---

## 1. Understanding the Problem

Input: array nums1 and nums2
Output: array containing their intersection
Constraints:
  - 1 <= nums1.length, nums2.length <= 1000
  - 0 <= nums1[i], nums2[i] <= 1000
Key observation: The elements in the result do not have to be unique (can appear as many times as the number of intersections)

---

## 2. Brute Force Approach

- Idea: Compare each number in the two arrays and append the numbers that appear in both arrays into a separate array
- Steps:
    - Create an empty array intersection
    - Loop through each number in nums1
    - For each number, check if it exists in nums2
    - If it exists, append to the intersection
    - remove integer from num2 so that it's not reused
- Time Complexity: O(n × m)
- Why it's inefficient: It would take too long when comparing large arrays

---

## 3. Optimised Approach

- Idea: use a Hash map to store frequencies, as duplicates are allowed in the intersection array
- Why it works:
   - A dictionary stores how many times each number appears
   - Ensures elements are only used the correct number of times
- Steps:
     - if loop to choose the smaller array (minimises space)
     - Create a dictionary to store frequencies of elements in the smaller array
     - Loop through the smaller array and count occurrences
     - Loop through the larger array
     - If a number exists in the dictionary and its count is greater than 0:
        - Append it to the Intersection array
        - Decrease its count in the dictionary
     - Return intersection array
- Time complexity: O(n + m)
  
---

## 4. Code Link
Press [IntersectionOfTwoArrays2](https://github.com/Amoraaa04/leetcode-solutions/blob/f203db95f2f0cb6347ea129c653443942fd74716/Python/IntersectionofTwoarrays2.py) to view code
