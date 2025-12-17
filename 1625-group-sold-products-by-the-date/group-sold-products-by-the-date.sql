-- # Write your MySQL query statement below
-- select  A1.sell_date  ,A1.product
-- from Activities A1
-- join Activities A2
-- on A1.sell_date  =A2.sell_date  
-- group by A1.sell_date,A1.product
-- | sell_date  | product    |
-- | ---------- | ---------- |
-- | 2020-05-30 | T-Shirt    |
-- | 2020-05-30 | Basketball |
-- | 2020-05-30 | Headphone  |
-- | 2020-06-01 | Bible      |
-- | 2020-06-01 | Pencil     |
-- | 2020-06-02 | Mask       |


SELECT
    sell_date,
    COUNT(DISTINCT product) AS num_sold,
    GROUP_CONCAT(
        DISTINCT product
        ORDER BY product
        SEPARATOR ','
    ) AS products
FROM Activities
GROUP BY sell_date
ORDER BY sell_date;
