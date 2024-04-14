-- Write your PostgreSQL query statement below


with cte as (select user1_id, user2_id from friendship
union all
select user2_id as user1_id, user1_id as user2_id from friendship)

select c1.user1_id, c2.user1_id as user2_id, count(*) as common_friend from cte c1 join cte c2 on c1.user1_id < c2.user1_id and c1.user2_id = c2.user2_id and (c1.user1_id, c2.user1_id) in (select * from friendship)
group by c1.user1_id, c2.user1_id having count(*) > 2

-- with cte as (select user1_id as person, user2_id as friend from friendship
-- union all
-- select user2_id as person, user1_id as friend from friendship)

-- select c1.person as user1_id, c2.person as user2_id, count(*) as common_friend from cte c1 join cte c2 on c1.person < c2.person and c1.friend = c2.friend and (c1.person, c2.person) in (select * from friendship)
-- group by c1.person, c2.person having count(*) >2