# Write your MySQL query statement below

SELECT max(salary) as SecondHighestSalary from employee where salary not in (select max(salary) from employee)