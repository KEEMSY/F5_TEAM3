curl -X 'POST' \
  'http://localhost:8000/articles/like/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "user_id": '$1',
  "article_id": 54
}'