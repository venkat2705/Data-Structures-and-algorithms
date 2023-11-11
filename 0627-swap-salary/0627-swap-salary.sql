# Write your MySQL query statement below

update salary SET sex =
case sex WHEN 'm' then 'f' else 'm' end
