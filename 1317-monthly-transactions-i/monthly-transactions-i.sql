# Write your MySQL query statement below


#one table for number of transactions, total amount
#one table for number of approved transactions, total amount
#join on contry and month

WITH all_tx AS (
  SELECT
    DATE_FORMAT(trans_date, '%Y-%m') AS month,
    country,
    COUNT(*) AS trans_count,
    SUM(amount) AS trans_total_amount
  FROM Transactions
  GROUP BY DATE_FORMAT(trans_date, '%Y-%m'), country
),
appr_tx AS (
  SELECT
    DATE_FORMAT(trans_date, '%Y-%m') AS month,
    country,
    COUNT(*) AS approved_count,
    SUM(amount) AS approved_total_amount
  FROM Transactions
  WHERE state = 'approved'
  GROUP BY DATE_FORMAT(trans_date, '%Y-%m'), country
)

SELECT all_tx.month, all_tx.country, trans_count, COALESCE(approved_count, 0) as approved_count, trans_total_amount, COALESCE(approved_total_amount, 0) as approved_total_amount
FROM all_tx LEFT JOIN appr_tx on all_tx.country <=> appr_tx.country AND all_tx.month = appr_tx.month