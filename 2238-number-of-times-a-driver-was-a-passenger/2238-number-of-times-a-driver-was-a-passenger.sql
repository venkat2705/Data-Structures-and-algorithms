# Write your MySQL query statement below

with driver as (
select distinct driver_id
from rides)

select driver.driver_id, count(passenger_id) cnt
from driver left join rides
on driver.driver_id = rides.passenger_id
group by driver.driver_id