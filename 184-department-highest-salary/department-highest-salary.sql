# Write your MySQL query statement below
SELECT Department.name AS Department, Employee.name AS Employee, Employee.salary AS Salary
FROM Employee
JOIN Department
ON Employee.departmentId = Department.id
JOIN(
    SELECT departmentId, MAX(salary) AS max_salary
    FROM Employee
    GROUP BY departmentId
    
) AS m
ON Employee.departmentId = m.departmentId AND Employee.salary = m.max_salary

