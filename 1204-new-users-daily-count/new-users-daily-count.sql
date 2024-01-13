
with cte as (select *,min(activity_date) mn_date from traffic
where activity = 'login' group by user_id)

select mn_date as login_date, count(user_id) as user_count from cte where mn_date between '2019-04-01' and '2019-06-30' group by mn_date 

