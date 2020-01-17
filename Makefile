topypi:
	poetry publish -r test

install:
	poetry install

lint:
	poetry run flake8 gen_diff

test:
	poetry run pytest --cov tests/
