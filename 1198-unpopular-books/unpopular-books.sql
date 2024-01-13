# Write your MySQL query statement below

with cte as (select * from orders where dispatch_date > "2018-06-23"),

cte2 as (select b.*,ifnull(sum(quantity),0) as sm from books b left join cte c on b.book_id = c.book_id where available_from < "2019-05-23" group by book_id having sm<10)

select book_id, name from cte2