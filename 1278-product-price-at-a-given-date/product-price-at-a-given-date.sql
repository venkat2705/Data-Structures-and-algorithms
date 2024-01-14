# Write your MySQL query statement below
WITH CTE AS (SELECT *, RANK() OVER(PARTITION BY product_id ORDER BY change_date DESC) as rnk FROM Products WHERE change_date <= "2019-08-16")

SELECT p.product_id, IFNULL(c.new_price,10) as price FROM CTE c RIGHT JOIN products p on p.product_id = c.product_id where c.rnk = 1 or c.rnk IS NULL GROUP BY p.product_id

