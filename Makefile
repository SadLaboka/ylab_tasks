test:
	poetry run pytest
lint:
	poetry run flake8 ylab_tasks
	poetry run flake8 tests
coverage:
	poetry run pytest --cov=ylab_tasks --cov-report=xml
install:
	poetry install
