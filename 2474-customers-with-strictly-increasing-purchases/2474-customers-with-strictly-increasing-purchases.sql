# Write your MySQL query statement below

with cte as (
    select customer_id, year(order_date) yr, lag(year(order_date)) over (partition by customer_id order by year(order_date)) last_year,
        rank() over (partition by customer_id order by year(order_date)) rnk_year, rank() over (partition by customer_id order by sum(price)) rnk_price
    from Orders
    group by 1, 2
)

select distinct customer_id from cte 
where customer_id not in (select customer_id from cte where last_year is not null and ((yr-last_year != 1) or rnk_year!=rnk_price))

