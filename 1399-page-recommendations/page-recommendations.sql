# Write your MySQL query statement below

with cte as (select user1_id as person, user2_id as friend from friendship where user1_id  = 1
union all
select user2_id as person, user1_id as friend from friendship where user2_id = 1)

select distinct page_id as recommended_page from likes where user_id in (select friend from cte) 
and page_id not in (select page_id from likes where user_id = 1)













-- WITH cte AS (SELECT user1_id, user2_id FROM Friendship where user1_id = 1
-- union all
-- SELECT user2_id as user1_id, user1_id as user2_id FROM Friendship where user2_id = 1)

-- SELECT distinct page_id as recommended_page
-- FROM Likes 
-- where user_id in (SELECT user2_id FROM cte)
-- AND page_id not in (SELECT page_id FROM likes WHERE user_id = 1)
