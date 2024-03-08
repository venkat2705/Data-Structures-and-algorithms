# Write your MySQL query statement below

-- select a.name, l.*, row_number() over(partition by l.id) as rn from logins l join accounts a on l.id = a.id 
SELECT DISTINCT l1.id,
(select name from accounts where id = l1.id) name 
from logins l1 join logins l2 
on l1.id = l2.id and datediff(l2.login_date, l1.login_date) between 1 and 4
group by l1.id,l1.login_date
having count(distinct l2.login_date) = 4














-- SELECT DISTINCT l1.id,
-- (select name from accounts where id = l1.id) name 
-- from logins l1 join logins l2 
-- on l1.id = l2.id and datediff(l2.login_date, l1.login_date) between 1 and 4 
-- group by l1.id,l1.login_date
-- having count(distinct l2.login_date) = 4
