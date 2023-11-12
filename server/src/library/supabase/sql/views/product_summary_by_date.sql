DROP VIEW IF EXISTS product_summary_by_date;
CREATE VIEW product_summary_by_date AS
SELECT *
FROM product_reviews_summary prs
INNER JOIN (
  SELECT product_id AS p_id, MAX(updated_at) AS max_updated_at
  FROM product_reviews_summary
  GROUP BY product_id
) prs_max 
ON prs.product_id = prs_max.p_id 
AND prs.updated_at = prs_max.max_updated_at;

