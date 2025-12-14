# Write your MySQL query statement below
select name
from SalesPerson p
where sales_id not in  ( select sales_id  from Company c  join Orders o  on o.com_id=c.com_id  where c.name like "RED" ) 


