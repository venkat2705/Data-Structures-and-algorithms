# Write your MySQL query statement below

-- Select date_format(trans_date,"%Y-%m") as month, country, sum(amount) as sm from transactions where state = "approved" group by date_format(trans_date,"%Y-%m"), country

with cte as (SELECT LEFT(c.trans_date,7) as month,country,'back' as state, amount from transactions t join chargebacks c on t.id=c.trans_id
UNION ALL
SELECT LEFT(trans_date,7) as month,country,state,amount from transactions where state='approved')

select month, country, 
SUM(CASE WHEN state = 'approved' then 1 else 0 end) as approved_count, 
SUM(CASE WHEN state = 'approved' then amount else 0 end) as approved_amount,
SUM(CASE WHEN state = 'back' then 1 else 0 end) as chargeback_count,
SUM(CASE WHEN state = 'back' then amount else 0 end) as chargeback_amount
from cte group by month, country


-- select * from cte


















-- with cte as 
-- (SELECT LEFT(c.trans_date,7) as month,country,'back' as state,amount from transactions t join chargebacks c on t.id=c.trans_id
-- UNION ALL
-- SELECT date_format(trans_date,"%Y-%m") as month,country,state,amount from transactions where state='approved'
-- )

-- SELECT month,country, 
-- sum(case when state = 'approved' then 1 else 0 end) as approved_count,
-- sum(case when state = 'approved' then amount else 0 end) as approved_amount,
-- sum(case when state = 'back' then 1 else 0 end) as chargeback_count,
-- sum(case when state = 'back' then amount else 0 end) as chargeback_amount
-- FROM cte 
-- group by month, country 
