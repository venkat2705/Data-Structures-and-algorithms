# Write your MySQL query statement below

with cte as (Select count(distinct session_id) as cnt from activity where activity_date between '2019-06-28' and '2019-07-27' group by user_id)

#select ifnull(round(avg(cnt),2),0) as average_sessions_per_user from cte
select ifnull(round(avg(cnt),2),0) as average_sessions_per_user from cte