# Write your MySQL query statement below
select Q.query_name ,ROUND(avg(Q.rating/position),2)as quality,  round(((SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END) /count(*))*100),2)as poor_query_percentage
from Queries as Q

group by Q.query_name