
SELECT e.name AS 'Employee'
FROM Employee e
JOIN Employee m  -- Used self join to compare manager and employee id's
ON e.managerID = m.id
WHERE e.salary > m.salary;

