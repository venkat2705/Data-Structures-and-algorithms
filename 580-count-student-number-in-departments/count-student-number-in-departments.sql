# Write your MySQL query statement below

with cte as (select dept_id, count(*) as cnt from student group by dept_id) 

select dept_name, ifnull(cnt,0) as student_number from department d left join cte c on d.dept_id = c.dept_id order by student_number desc, dept_name