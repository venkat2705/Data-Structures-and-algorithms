# Write your MySQL query statement below

with cte as (select p.*, experience_years, rank() over(partition by project_id order by experience_years desc) rnk from project p left join employee e on p.employee_id = e.employee_id)

select project_id,employee_id from cte where rnk = 1















# with cte as (select project_id, p.employee_id, experience_years, max(experience_years) over(partition by project_id ) as YOE from project p join employee e on p.employee_id = e.employee_id)

# select project_id, employee_id from cte where experience_years = YOE