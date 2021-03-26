.DEFAULT_GOAL := help

clean: ## Clean project files
	rm -rf *.egg-info
	rm -rf dist
	rm -rf gradle_profiler_pttest/__pycache__
	rm -rf tests/__pycache__
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf coverage.xml

setup: ## Install dependencies
	poetry install

inspect: ## Run code style checks
	python -m pip install flake8
	flake8 gradle_profiler_pttest tests

test: ## Run unit and integration tests
	poetry run pytest -vv --cov-report=xml --cov=gradle_profiler_pttest tests

build: ## Package this project in wheels/zip formats
	poetry build

run: ## Run this project. Accepts baseline and modified as arguments
	poetry run gradle-profiler-pttest -b $(baseline) -m $(modified)

deploy: ## Deploy the current build to Pypi
	poetry config pypi-token.pypi $(token)
	poetry build
	poetry publish

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) |\
		sort |\
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
