# Makefile
install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --force-reinstall --user dist/*.whl

test:
	poetry run pytest

test-coverage-xml:
	poetry run pytest --cov=gendiff --cov-report xml

lint:
	poetry run flake8 gendiff
