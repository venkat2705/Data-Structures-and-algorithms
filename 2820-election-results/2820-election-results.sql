# Write your MySQL query statement below

with cte as (select *, round(1/count(voter) over(partition by voter),2) as num_votes from votes),

cte2 as (select candidate, sum(num_votes) as sum_votes from cte group by candidate order by sum(num_votes) desc)

select candidate from cte2 where sum_votes in (select max(sum_votes) from cte2) order by candidate 



