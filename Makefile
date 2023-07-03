LOCAL := poetry run python manage.py

install:
	poetry install

migrations:
	$(LOCAL) makemigrations

migrate:
	$(LOCAL) migrate

setup:
	cp -n .env.example .env || true
	make install
	make migrations
	make migrate

PORT ?= 8000
start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) it_bell_news.wsgi

dev:
	$(LOCAL) runserver 0.0.0.0:8080

check:
	poetry check

lint:
	poetry run flake8

test:
	$(LOCAL) test

test-coverage:
	$(LOCAL) test
	poetry run coverage report -m --omit='*/python-project-83/*'
	poetry run coverage xml --omit='*/python-project-83/*'

