# Plus one

Problem Summary: Given an integer represented as an array of digits, increment the integer by one and return the resulting array of digits.

---

## 1. Understanding the Problem
- Input: List of digits representing an array [1, 2, 3]
- Output: New list of digits representing the integer plus one [1, 2, 4]
- Constraints:
   - Should return the same array
- Key observation: Only numbers < 9 stop the carry, but 9s become 0, and the loop continues
   
---

## 2. Brute Force Approach
- Idea: could create a new list and try to build the incremented number by adding 1 to the last digit and handling carries manually.
**Note:** I wasn’t sure how to implement this at first — would need to research other brute-force methods.
- Steps:
- Time Complexity:
- Why it's inefficient: it usually requires more space and steps 

---

## 3. Optimised Approach
- Idea:
    - Modify the original list
    - any digit that is 9 becomes 0 
    - if the first digit less than 9 is incremented by 1, then the loop stops
    - If all digits are 9, add a 1 at the front
- Why it works:
     -  only adds a new digit if necessary
     -  Processes digits by least significant first
- Steps:
   1. Create a for loop that is the length of the list
   2. iterates from the end of the list to the front 
   3. if loop that adds 1 to the digit if < 9
        - else: if digit == 9 it ( set to 0 and continue to the next left-most digit)
        - If all digits are 9, then 1 is added to the rightmost side after the loop
- Time complexity: O(n) - n is the number of digits.

---

## Code Implementation
[Plus One code]()

## Key takeaways
- practice more / explore brute-force ideas
