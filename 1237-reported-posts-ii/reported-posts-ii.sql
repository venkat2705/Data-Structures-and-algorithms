# Write your MySQL query statement below

with cte as (select count(distinct r.post_id)/count(distinct a.post_id) as cnt from actions a left join removals r on a.post_id = r.post_id where extra = 'spam' group by a.action_date)

select round(avg(cnt)*100,2) as average_daily_percent from cte 

















-- with cte as (Select count(distinct r.post_id)/count(distinct a.post_id) as cnt from actions a left join removals r on a.post_id = r.post_id where extra = 'spam' group by a.action_date)

-- select round(avg(cnt)*100,2) as average_daily_percent from cte 