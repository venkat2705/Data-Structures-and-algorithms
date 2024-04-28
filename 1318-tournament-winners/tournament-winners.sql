# Write your MySQL query statement below

with cte as (select player_id, group_id, sum(case when player_id = first_player then first_score when player_id = second_player then second_score end) as score from players p join matches m on p.player_id = m.first_player or p.player_id = m.second_player group by player_id),

cte2 as (select group_id, player_id, rank() over(partition by group_id order by score desc, player_id) as rn from cte)

select group_id, player_id from cte2 where rn = 1












-- with cte1 as (select p.*, sum(case when p.player_id = m.first_player then m.first_score else m.second_score end) as tot_points from players p join matches m  on p.player_id in (m.first_player or m.second_player)
-- ),

-- cte2 as (select p.*,rank() over(partition by group_id order by tot_points desc, player_id) as rnk from players p join cte1 on p.player_id = cte1.player_id)

-- select group_id, player_id from cte2 where rnk = 1