# Write your MySQL query statement below

with cte as (select *, rank() over(partition by product_id order by year) as rnk from sales)

select product_id, year as first_year, quantity, price from cte where rnk = 1