# Write your MySQL query statement below


with cte as (select *, max(salary) over(partition by company_id) as max_sal from salaries)

select company_id, employee_id, employee_name, 
case 
when max_sal < 1000 then salary
when max_sal >= 1000 and max_sal <= 10000 then round(salary*0.76)
when max_sal > 10000 then round(salary*0.51)
end as salary
from cte









-- select company_id, employee_id, employee_name, 
-- (case when max(salary) over(partition by company_id) < 1000 then salary 
-- when max(salary) over(partition by company_id) > 10000 then round(salary*0.51)
-- else round(salary*0.76)
-- end) as salary from salaries
