-- Problem: Given the User and Rides table, calculate the distance travelled by each user.
-- Order by travelled_distance DESC, then by name ASC

SELECT 
     name, 
       CASE 
         WHEN SUM(distance) IS NULL THEN 0
         ELSE SUM(r.distance)
       END AS travelled_distance
FROM Users u
LEFT JOIN Rides r
ON u.id = r.user_id
GROUP BY u.id, u.name
ORDER BY travelled_distance DESC, name ASC;
