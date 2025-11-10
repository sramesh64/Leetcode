# Write your MySQL query statement below

#want table that is product_id, purchase_date, units, price

SELECT Prices.product_id, COALESCE(ROUND(SUM(Prices.price * UnitsSold.units) / SUM(UnitsSold.units), 2), 0) AS average_price
FROM Prices
LEFT JOIN UnitsSold ON purchase_date BETWEEN start_date AND end_date AND Prices.product_id = UnitsSold.product_id
GROUP BY Prices.product_id