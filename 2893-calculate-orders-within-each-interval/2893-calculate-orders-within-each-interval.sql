# Write your MySQL query statement below


with cte as (select minute, order_count, 
    if(minute % 6 != 0, minute div 6 + 1,  minute div 6) as interval_no
    from orders)

select interval_no, sum(order_count) as total_orders from cte group by interval_no order by interval_no