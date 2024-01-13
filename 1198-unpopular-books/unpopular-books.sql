# Write your MySQL query statement below

with cte as (select * from orders where dispatch_date > "2018-06-23"),

cte2 as (select b.*,ifnull(sum(quantity),0) as sm from books b left join cte c on b.book_id = c.book_id where available_from < "2019-05-23" group by book_id having sm<10)

select book_id, name from cte2
















# with j as (select b.*, o.order_id, o.quantity, o.dispatch_date
#             from books b
#             inner join orders o
#             on b.book_id = o.book_id
#             )
# , a as (select book_id, sum(quantity) as sold
#             from j
#             where dispatch_date >= '2018-06-23'
#             group by book_id)
# , b as (select b.*, a.sold
#             from books b
#             left join a
#             on b.book_id = a.book_id
#            )
# select distinct book_id, name 
# from b where ((sold is null) or (sold<10))
# and book_id not in (select book_id from books where available_from >= '2019-05-23' )
