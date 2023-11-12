DROP VIEW IF EXISTS reviews_full_details;
CREATE VIEW reviews_full_details AS
select
  r.id as review_id,
  r.content,
  r.number_helpful, 
  r.rating,
  r.review_date,
  r.images,
  r.source_url,
  prod.id as product_id,
  prod.product_name,
  users.id as user_id,
  users.name as user_name
from
  -- review_tag_managers rtm
  reviews r 
  left join products prod on r.product_id = prod.id
  left join users  on r.user_id = users.id