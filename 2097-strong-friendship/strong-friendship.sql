# Write your MySQL query statement below

with cte as (select user1_id as person, user2_id as friend from friendship
union
select user2_id as person, user1_id as friend from friendship)

select c1.person as user1_id, c2.person as user2_id, count(*) as common_friend 
from cte c1 join cte c2 on c1.person < c2.person and c1.friend  = c2.friend 
and (c1.person,c2.person) in (select * from friendship)
group by c1.person,c2.person having common_friend>=3
















-- with cte as (select user1_id as person, user2_id as friend from friendship
-- union
-- select user2_id as person, user1_id as friend from friendship)

-- select c1.person as user1_id, c2.person as user2_id, count(*) as common_friend 
-- from cte c1 join cte c2 on c1.person < c2.person and c1.friend  = c2.friend 
-- and (c1.person,c2.person) in (select * from friendship)
-- group by c1.person,c2.person having common_friend>=3