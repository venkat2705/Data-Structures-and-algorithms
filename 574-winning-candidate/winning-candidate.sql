# Write your MySQL query statement below

with cte as (select v.*, c.name, count(v.candidateId) as cnt from vote v join candidate c on v.candidateId = c.id group by v.candidateId order by cnt desc)

select name from cte limit 1



















# with cte as (select candidateid,count(*) as cnt from vote group by candidateid order by cnt desc limit 1)

# select name from candidate where id in (select candidateid from cte)



























# with cte as (select candidateid,c.name, count(*) cnt from vote v join candidate c on c.id = v.candidateid group by candidateId)

# select name from cte where cnt = (select max(cnt) from cte)
