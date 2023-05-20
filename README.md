after start docker-compose 
alembic revision --autogenerate -m 'Init db' - инит базы
docker-compose exec app pytest . - тесты