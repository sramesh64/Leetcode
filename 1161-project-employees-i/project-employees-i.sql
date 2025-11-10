# Write your MySQL query statement below
-- Write an SQL query that reports the average experience years of all the employees for each project, rounded to 2 digits.

#first want project_id, employee_id, years

SELECT project_id, ROUND(AVG(experience_years), 2) AS average_years
FROM Project
JOIN Employee
ON Project.employee_id = Employee.employee_id
GROUP BY project_id