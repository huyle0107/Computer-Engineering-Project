DROP VIEW IF EXISTS product_ratings;
CREATE VIEW product_ratings AS
SELECT product_id, rating, DATE(updated_at) AS updated_at, active, COUNT(*) AS total
FROM reviews
WHERE rating IS NOT NULL and active IS true
GROUP BY product_id, rating, DATE(updated_at), active;
