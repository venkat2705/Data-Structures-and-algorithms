# Write your MySQL query statement below

Select t.team_id, t.team_name, 
sum(case when team_id = host_team and host_goals > guest_goals then 3
when team_id = guest_team and host_goals < guest_goals then 3
when host_goals = guest_goals then 1
else 0 end) as num_points from teams t left join matches m on m.host_team = t.team_id or t.team_id = m.guest_team
group by t.team_id order by num_points desc, t.team_id