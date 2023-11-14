# Write your MySQL query statement below

with cte as (
SELECT *, ROW_NUMBER() OVER(PARTITION BY COMPANY ORDER BY Salary ASC, Id ASC) AS RN_ASC,
ROW_NUMBER() OVER(PARTITION BY COMPANY ORDER BY Salary DESC, Id DESC) AS RN_DESC
FROM Employee)


select id,company,salary from cte where RN_ASC BETWEEN RN_DESC-1 AND RN_DESC+1
ORDER BY company, Salary


