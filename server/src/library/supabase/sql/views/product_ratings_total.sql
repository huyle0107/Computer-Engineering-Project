DROP VIEW IF EXISTS product_ratings_total;
CREATE VIEW product_ratings_total AS
SELECT product_id, DATE(updated_at) AS updated_at, active, COUNT(*) AS total
FROM reviews
WHERE rating IS NOT NULL and active IS true
GROUP BY product_id, DATE(updated_at), active;
