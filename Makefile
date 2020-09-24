clean:
	rm -rf *.egg-info
	rm -rf dist
	rm -rf gradle_profiler_pttest/__pycache__
	rm -rf tests/__pycache__
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf coverage.xml

setup:
	poetry install

inspect:
	flake8 gradle_profiler_pttest tests

test:
	poetry run pytest -vv --cov-report=xml --cov=gradle_profiler_pttest tests

build:
	poetry build

run:
	poetry run gradle-profiler-pttest -b $(baseline) -m $(modified)

pypiconfig:
	poetry config pypi-token.pypi $(token)

deploy:
	poetry build
	poetry publish
