# Write your MySQL query statement below

with cte as (select customer_id, name, visited_on, sum(amount) as amount from customer group by visited_on order by visited_on),

cte2 as (select visited_on, 
sum(amount) over(ORDER BY visited_on RANGE BETWEEN INTERVAL '6' DAY PRECEDING AND CURRENT ROW) as amount, 
round(avg(amount) over(ORDER BY visited_on RANGE BETWEEN INTERVAL '6' DAY PRECEDING AND CURRENT ROW),2)
as average,row_number() over(order by visited_on) as rn from cte )

# select * from cte2

select visited_on, amount, average as average_amount from cte2 where visited_on>'2019-01-06' and rn > 6 order by visited_on  
# select * from cte2





















# with cte as (select customer_id,name,visited_on,sum(amount) as amount from customer where visited_on>=(select min(visited_on) as mn from customer)+6 group by visited_on),

# cte2 as (select visited_on, sum(amount) as amt from customer where visited_on not in (select visited_on from cte))

# select visited_on,
# #(select amt from cte2) + amount, 
# round(((select amt from cte2) + amount)/7,2) as average_amount
# from cte
# group by visited_on
# order by visited_on

