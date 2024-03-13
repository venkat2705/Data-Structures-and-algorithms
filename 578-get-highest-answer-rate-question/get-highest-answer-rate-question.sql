# Write your MySQL query statement below

WITH cte AS (SELECT question_id, 
SUM(CASE WHEN action = 'answer' THEN 1 ELSE 0 END) / SUM(CASE WHEN action = 'show' THEN 1 ELSE 0 END) as ratio FROM SurveyLog GROUP BY question_id)


SELECT question_id as survey_log from cte ORDER BY ratio desc, question_id LIMIT 1 











-- with cte as (select question_id, sum(CASE WHEN action = 'answer' then 1 else 0 end) / sum(CASE WHEN action = 'show' then 1 else 0 end) as answer_cnt from surveylog group by question_id)

-- select question_id as survey_log from cte order by answer_cnt desc, question_id limit 1


