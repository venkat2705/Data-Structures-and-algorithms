# Write your MySQL query statement below

with cte as (SELECT s.*, sum(s.quantity * p.price) as amount_spent from sales s join product p on s.product_id = p.product_id group by user_id,product_id),

cte2 as (select user_id, product_id, sum(amount_spent) as amount_spent, max(amount_spent) over(partition by user_id) as mx from cte 
group by user_id,product_id)

select user_id, product_id from cte2 where amount_spent = mx


