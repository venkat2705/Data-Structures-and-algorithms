# Write your MySQL query statement below


with cte as (select user1_id as person, user2_id as friend from friendship
union all
select user2_id as person, user1_id as friend from friendship)

select  distinct page_id as recommended_page from likes where user_id in (select friend from cte where person = 1) and page_id not in (select page_id from likes where user_id = 1)















-- with cte as (select user1_id as person, user2_id as friend from friendship where user1_id  = 1
-- union all
-- select user2_id as person, user1_id as friend from friendship where user2_id = 1)

-- select distinct page_id as recommended_page from likes where user_id in (select friend from cte) 
-- and page_id not in (select page_id from likes where user_id = 1)
