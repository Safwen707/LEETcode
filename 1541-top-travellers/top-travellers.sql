# Write your MySQL query statement below
select name,  Ifnull(sum(distance),0)   as travelled_distance
from Users U
Left join Rides R
on R.user_id  =U.id
group by R.user_id  
order by travelled_distance desc, name asc

