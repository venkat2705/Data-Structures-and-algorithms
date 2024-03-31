# Write your MySQL query statement below

with cte as (select machine_id, sum(Case when activity_type = 'end' then timestamp else 0 end) as sum_end,  sum(Case when activity_type = 'start' then timestamp else 0 end) as sum_start, count(distinct process_id) as cnt  from activity group by machine_id)

select machine_id, round((sum_end - sum_start)/cnt,3) as processing_time from cte














-- select a1.machine_id, ROUND(AVG(a2.timestamp - a1.timestamp), 3) as processing_time
-- from Activity a1
-- inner join Activity a2
-- on a1.process_id = a2.process_id
-- and a1.machine_id = a2.machine_id
-- and a1.timestamp < a2.timestamp
-- group by a1.machine_id;