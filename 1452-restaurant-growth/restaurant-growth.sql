# Write your MySQL query statement below

with cte as (select customer_id, name, visited_on, sum(amount) as amount from customer group by visited_on order by visited_on),

cte2 as (select visited_on, 
sum(amount) over(ORDER BY visited_on RANGE BETWEEN INTERVAL '6' DAY PRECEDING AND CURRENT ROW) as amount, 
row_number() over(order by visited_on) as rn from cte )


select visited_on, amount, round(amount/7,2) as average_amount from cte2 where rn > 6 order by visited_on  





















# with cte as (select customer_id,name,visited_on,sum(amount) as amount from customer where visited_on>=(select min(visited_on) as mn from customer)+6 group by visited_on),

# cte2 as (select visited_on, sum(amount) as amt from customer where visited_on not in (select visited_on from cte))

# select visited_on,
# #(select amt from cte2) + amount, 
# round(((select amt from cte2) + amount)/7,2) as average_amount
# from cte
# group by visited_on
# order by visited_on

