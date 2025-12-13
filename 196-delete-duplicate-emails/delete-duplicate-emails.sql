# Write your MySQL query statement below
DELETE FROM Person WHERE id not in (select id from (select email,min(id) as id from Person  group by email ) as r);