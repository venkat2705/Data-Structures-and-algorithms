# Write your MySQL query statement below

with cte1 as (select customer_id, name, visited_on, sum(amount) as amount from customer group by visited_on order by visited_on),

cte2 as (select visited_on, sum(amount) over(order by visited_on range between interval '6' day preceding and current row) as amount, row_number() over(order by visited_on) as rn from cte1)

select distinct visited_on, amount, round(amount/7, 2) as average_amount from cte2 where rn > 6 order by visited_on



