-- sql/data_quality_queries.sql
-- 1. Null counts
SELECT
SUM(CASE WHEN amount IS NULL THEN 1 ELSE 0 END) AS amount_nulls,
SUM(CASE WHEN email IS NULL THEN 1 ELSE 0 END) AS email_nulls
FROM transactions;


-- 2. Duplicate tx
SELECT tx_id, COUNT(*) c FROM transactions GROUP BY tx_id HAVING c>1;
