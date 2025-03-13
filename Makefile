.PHONY: format lint mypy

DOCKER_COMPOSE_RUN=docker exec -it password_manager_app

format:
	$(DOCKER_COMPOSE_RUN) black /app/app/api/v1/controllers /app/app/api/v1/crud /app/app/api/v1/models /app/app/api/v1/schemas /app/app/api/v1/usecases

lint:
	$(DOCKER_COMPOSE_RUN) flake8 /app/app/api/v1/controllers /app/app/api/v1/crud /app/app/api/v1/models /app/app/api/v1/schemas /app/app/api/v1/usecases

mypy:
	$(DOCKER_COMPOSE_RUN) mypy /app/app/api/v1/controllers /app/app/api/v1/crud /app/app/api/v1/models /app/app/api/v1/schemas /app/app/api/v1/usecases

check: format lint mypy
