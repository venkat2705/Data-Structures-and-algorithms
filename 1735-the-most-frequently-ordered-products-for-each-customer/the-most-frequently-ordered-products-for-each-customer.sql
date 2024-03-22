# Write your MySQL query statement below

with cte as (select o.customer_id, o.product_id, p.product_name, rank() over(partition by customer_id order by count(*) desc) as rnk from orders o join products p on o.product_id = p.product_id group by customer_id, product_id)

-- cte2 as (select *, rank() over(partition by customer_id order by cnt desc) as rnk from cte)

select customer_id, product_id, product_name from cte where rnk = 1