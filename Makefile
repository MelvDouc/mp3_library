.PHONY: run run-dev freeze-reqs

PROJECT_NAME = mp3_library

run:
	docker compose up --build

run-dev:
	python3 -m src.$(PROJECT_NAME)

freeze-reqs:
	python3 -m pip freeze > requirements.txt