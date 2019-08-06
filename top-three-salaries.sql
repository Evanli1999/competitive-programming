/* https://leetcode.com/problems/department-top-three-salaries/submissions/
/* Write your T-SQL query statement below */
WITH ordered AS (
    SELECT 
        d.Name as Department,
        e.name as Employee,
        e.salary as Salary,

        DENSE_RANK() OVER (PARTITION BY DepartmentId ORDER BY Salary DESC) as dept_salary_ranking

    FROM employee e INNER JOIN department d on e.DepartmentId = d.Id
)

SELECT Department, Employee, Salary FROM ordered WHERE dept_salary_ranking < 4
