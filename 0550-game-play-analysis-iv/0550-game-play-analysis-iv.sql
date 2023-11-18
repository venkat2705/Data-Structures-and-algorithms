# Write your MySQL query statement below

WITH CTE as (SELECT *,dense_rank() over(partition by player_id ORDER BY event_date) AS rnk FROM activity )

SELECT ROUND(count(c1.player_id)/(SELECT count(distinct player_id) FROM CTE),2) as fraction FROM CTE c1, CTE c2 
WHERE c1.rnk = 1 AND c1.player_id = c2.player_id AND datediff(c2.event_date,c1.event_date) = 1

