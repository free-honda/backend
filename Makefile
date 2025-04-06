up:
	docker compose up --build

up-d:
	docker compose up -d

ps:
	docker compose ps

logs:
	docker compose logs

exec app:
	docker exec -it fastapi-app bash

exec db:
	docker exec -it mysql-db bash

down:
	docker compose down