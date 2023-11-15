
with cte as (Select user_id, min(activity_date) as activity_date from traffic where  activity = 'login' group by user_id) 


select activity_date as login_date, count(*) as user_count from cte where  activity_date between '2019-04-01' and '2019-06-30' group by activity_date order by login_date 


