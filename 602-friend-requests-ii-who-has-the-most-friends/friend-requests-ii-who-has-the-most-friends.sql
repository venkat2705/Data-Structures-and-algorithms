#  # Write your MySQL query statement below

with cte as (select * from RequestAccepted
union all
select accepter_id as requester_id, requester_id as accepter_id, accept_date  from RequestAccepted)

select requester_id as id, count(*) as num from cte group by requester_id order by num desc LIMIT 1
















-- with cte as (select requester_id as f1, accepter_id as f2 from RequestAccepted
-- union all
-- select accepter_id as f1,  requester_id as f2 from RequestAccepted)

-- select f1 as id, count(f2) as num from cte group by f1 order by num desc limit  1
