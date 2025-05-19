.PHONY: run freeze-reqs

PROJECT_NAME = mp3_library

run:
	python3 -m src/(PROJECT_NAME)

freeze-reqs:
	python3 -m pip freeze > requirements.txt