# Write your MySQL query statement below

with cte as (select o.*, c.customer_name from orders o join customers c on c.customer_id = o.customer_id),

cte2 as (select *, sum(CASE WHEN product_name = 'A' then 1 else 0 end) as A_count, 
sum(CASE WHEN product_name = 'B' then 1 else 0 end) as B_count,
sum(CASE WHEN product_name != 'C' then 1 else 0 end) as C_count, count(*) as cnt from cte group by customer_name)

select customer_id, customer_name  from cte2 where A_count>0 and B_count>0 and C_count = cnt






























-- with cte as (select o.*, 
-- sum(case when o.product_name = 'A' then 1 else 0 end) as A,
-- sum(case when o.product_name = 'B' then 1 else 0 end) as B,
-- sum(case when o.product_name = 'C' then 1 else 0 end) as C,
-- c.customer_name from orders o join customers c on o.customer_id = c.customer_id group by o.customer_id)

-- select customer_id, customer_name from cte where A>=1 and B>=1 and c=0 order by customer_id

