# Write your MySQL query statement below

with cte as (select ad_id, sum(case when action = 'Clicked' then 1 else 0 end) as clicked_sum, 
sum(case when action = 'Clicked' then 1 else 0 end) + sum(case when action = 'Viewed' then 1 else 0 end) as total_sum from Ads group by ad_id)

select ad_id, round((case when total_sum = 0. then 0 else clicked_sum * 100/total_sum end),2) as ctr from cte order by ctr desc, ad_id

