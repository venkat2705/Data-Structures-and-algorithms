# Write your MySQL query statement below
with cte1 as (select tiv_2015 from insurance group by tiv_2015 having count(*)>1),

cte2 as (select lat,lon from insurance group by 1,2 having count(*)=1 )

select round(sum(tiv_2016),2) as tiv_2016 from insurance where tiv_2015 in (select * from cte1) and (lat,lon) in (select * from cte2)