-- Write a SQL query to get the first name and the max salary for each employee id

SELECT e.id, e.first_name, MAX(s.salary) AS max_salary
FROM employees e
INNER JOIN salaries s ON e.id = s.id
GROUP BY e.id, e.first_name




