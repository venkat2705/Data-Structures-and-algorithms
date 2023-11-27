# Write your MySQL query statement below

with cte as (select e.*, d.name as d_name, dense_rank() over(partition by e.departmentId order by salary desc) as rnk from employee e join department d on e.departmentId = d.id)

select d_name as Department, name as Employee, salary from cte where rnk<=3