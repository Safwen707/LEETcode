# Write your MySQL query statement below
select EU.unique_id as unique_id , name
from EmployeeUNI EU
right join Employees E
on EU.id=E.id
order by unique_id desc

