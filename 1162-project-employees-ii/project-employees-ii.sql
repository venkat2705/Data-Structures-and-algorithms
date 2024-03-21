# Write your MySQL query statement below

with cte as (select project_id, count(*) as cnt from project group by project_id)

select project_id from cte where cnt in (select max(cnt) from cte)