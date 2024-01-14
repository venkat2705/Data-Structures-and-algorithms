# Write your MySQL query statement below
WITH CTE AS (SELECT *, RANK() OVER(PARTITION BY product_id ORDER BY change_date DESC) as rnk FROM Products WHERE change_date <= "2019-08-16")

SELECT p.product_id, IFNULL(c.new_price,10) as price FROM CTE c RIGHT JOIN products p on p.product_id = c.product_id where c.rnk = 1 or c.rnk IS NULL GROUP BY p.product_id

# with cte as (select * from products where change_date <= '2019-08-16'), 
# cte2 as (select product_id,new_price, change_date, rank() over(partition by product_id order by change_date desc) as rn from cte)

# select * from cte2

# select p.product_id, ifnull(c.new_price , 10) as price
# from cte2 c right join products p on p.product_id = c.product_id 
# where c.rn = 1 or c.rn IS NULL group by p.product_id
 



