# Write your MySQL query statement below

with cte as (select question_id, sum(CASE WHEN action = 'answer' then 1 else 0 end) / sum(CASE WHEN action = 'show' then 1 else 0 end) as answer_cnt from surveylog group by question_id)

select question_id as survey_log from cte order by answer_cnt desc, question_id limit 1


