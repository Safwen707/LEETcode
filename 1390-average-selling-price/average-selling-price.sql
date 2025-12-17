# Write your MySQL query statement below
select p.product_id ,COALESCE((round(sum(units*price)/sum(units),2)),0) as average_price 
from Prices p
left join UnitsSold u 
on p.product_id=u.product_id 
AND u.purchase_date BETWEEN p.start_date AND p.end_date  
group by p.product_id