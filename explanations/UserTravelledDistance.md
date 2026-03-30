# User travelled distance
---
**Problem summary:**  Given `Users` and `Rides` tables, return the total distance travelled by each user. 
- Return 0 for users with no rides
- Order by travelled_distance DESC, then by name ASC
---

## 1. Understanding the Problem
- **Input:** Tables `Users(id, name)` and `Rides(id, user_id, distance)`  
- **Output:** Table with columns `name` and `travelled_distance`  (total travelled distance)
- **Constraints:** 
  - Users may have 0 or more rides
  - order by distance descending, then name ascending
**Key observation:** Use `LEFT JOIN` to include users without rides and handle `NULL` distances

---

## 3. Approach
- **Idea / Plan:** Aggregate rides per user using `SUM(distance)` and join with table `Users`  
- **Steps:** 
  - LEFT JOIN Users with Rides on `user_id`
  - SUM distances for each user
  - Use `CASE` to replace `NULL` with 0 (When users have not travelled a distance)
  - ORDER BY travelled_distance DESC, name ASC

--- 

## Code link
[UserTravelledDistance](https://example.com)
