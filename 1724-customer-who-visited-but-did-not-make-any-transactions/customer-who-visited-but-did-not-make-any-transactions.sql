# Write your MySQL query statement below

#step 1, get table of customer id, and visit id for every visit in which the customer didnt make transactoin

SELECT customer_id, count(*) AS count_no_trans FROM (
    SELECT visit_id, customer_id
    FROM Visits
    WHERE visit_id NOT IN(
        SELECT visit_id
        FROM TRANSACTIONS
    )
) AS A
GROUP BY customer_id