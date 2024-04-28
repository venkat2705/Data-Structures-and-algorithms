# Write your MySQL query statement below

with cte as (
--     SELECT 
--     Country.name AS country, sum(calls.duration) as dur
-- FROM Country
-- INNER JOIN Person
--     ON SUBSTRING(Person.phone_number, 1, 3) = Country.country_code
-- INNER JOIN Calls
--     ON Calls.caller_id = Person.id
--     OR Calls.callee_id = Person.id
--     group by country
    select p.id, c.name from person p join country c on left(p.phone_number,3) = c.country_code
    ),

cte2 as (select  name as country from cte  join calls c on cte.id = c.caller_id or cte.id = c.callee_id group by name having avg(duration) > (select avg(duration) from calls)) 

-- select name from cte2 having avg(dur) > (select avg(duration) from calls)

-- SELECT 
--     Country.name AS country
-- FROM Country
-- INNER JOIN Person
--     ON SUBSTRING(Person.phone_number, 1, 3) = Country.country_code
-- INNER JOIN Calls
--     ON Calls.caller_id = Person.id
--     OR Calls.callee_id = Person.id
-- GROUP BY Country.name
-- HAVING AVG(duration) > (SELECT AVG(duration) FROM Calls)

select * from cte2