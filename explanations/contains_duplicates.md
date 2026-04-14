# Contains duplicates

Problem summary: Given a list of numbers, return True if the array contains at least one duplicate

---

## 1. Understanding the Problem
- Input: array of integers
- Output: Boolean (True if it contains duplicates, False if not)
- Constraints:
   -  1 <= nums.length <= 10^5
   - 10^9 <= nums[i] <= 10^9
- Key observation:
   - In the example given, they use the same array
   - My answer must loop through the num array instead of creating another array

---

## 2. Brute Force Approach
- Idea: Compare every element in the array to  each element in the nums list
- Time Complexity: O(n²)
- Why it's inefficient: It will take a lot of time if the array contains many elements (e.g., more than 20)

---

## 3. Optimised Approach
- Idea: Sort the array, then compare adjacent elements 
- Why it works: All duplicates will be next to each other, meaning that we can loop through the list and compare each adjacent element
- Time complexity:  O(n log n)
  
---

## 4. Code Implementation 
Press [Contains duplicates](https://github.com/Amoraaa04/leetcode-solutions/blob/4fd63030296a06090ac1fb6f4bf8d44442081b7a/Python/contains_duplicates.py) to view code

---

## 5. Key Takeaways
- Sorting the array makes it easier to detect duplicates efficiently.
- Comparing adjacent elements is faster than checking every pair.
- Always consider the constraints (array size, element range) when choosing an approach.
- Thinking about time complexity helps decide the best method for large inputs.
- Using a structured approach (understand → brute force → optimise → implement) makes problem-solving clearer and easier to explain.
