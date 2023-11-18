# Write your MySQL query statement below

select dept_name, count(student_name) as student_number 
from department d left join student s on d.dept_id = s.dept_id 
group by d.dept_id 
order by student_number desc, dept_name
