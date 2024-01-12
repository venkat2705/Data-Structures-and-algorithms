# Write your MySQL query statement below

with cte as (select *,avg(occurences) over(partition by event_type) as avg_o from events)

select business_id from cte group by business_id having sum(case when occurences > avg_o then 1 else 0 end)>1

