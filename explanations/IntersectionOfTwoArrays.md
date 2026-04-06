# Intersection of Two Arrays

**Problem Summary:** Given two integer arrays, return an array of their intersection (return an array that contains the integers that are present in both arrays)

---

## 1. Understanding the Problem
- Input: array *nums1* and *nums2*
- Output: array containing their intersection
- Constraints:
 - 1 <= nums1.length, nums2.length <= 1000
 - 0 <= nums1[i], nums2[i] <= 1000
- Key observation: Each element in the result must be unique (no duplicates)

---

## 2. Brute Force Approach
- Idea: Compare the two arrays and append the numbers that appear in both arrays into a separate array
- Steps:
    - create an empty array *intersection*
    - Loop through each number in nums1
    - For each number, check if it exists in nums2
    - If it exists and is not already in the result, append to *intersection*
- Time Complexity: O(n × m)
- Why it's inefficient: It would take too long when comparing large arrays

---

## 3. Optimised Approach
- Idea: could use set and return values that are in *nums1* and *nums2*
- Why it works:
  - Sets remove duplicates automatically
  - Checking if a value exists in a set is O(1), which is much faster than a list (O(n)) 
- Steps:
   - turn *num1* into a set
   - create an empty set called *intersection*
   - Loop through nums2
   - Check if each value exists in the set of nums1
   - if number is in *num1*, add to *intersection*
   - return intersection
- Time complexity: O(n + m)

---

## 4. Code Link
Press [IntersectionOfTwoArrays](https://github.com/Amoraaa04/leetcode-solutions/blob/b97bd05cd07fd23ec6b223f2512d0f86917df6c2/Python/IntersectionOfTwoArrays.py) to view code
