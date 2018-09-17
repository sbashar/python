install:
	python3 -m pip install pipenv
	python3 -m pipenv install

install_dev:
	python3 -m pip install pipenv
	python3 -m pipenv install --dev

run_linter:
	python3 -m pipenv run pylint src tests

run_typechecker:
	python3 -m pipenv run mypy --strict --allow-untyped-decorators src tests

run_formatter:
	python3 -m pipenv run yapf -d -r -p src tests

run_unit_test:
	python3 -m pipenv run pytest -E unit tests

run_unit_test_with_cov:
	python3 -m pipenv run pytest -E unit tests --cov=src --cov-config .coveragerc

run_integration_test:
	python3 -m pipenv run pytest -E integration tests

run_integration_test_with_cov:
	python3 -m pipenv run pytest -E integration tests --cov=src --cov-config .coveragerc

check_hackerrank:
	make run_formatter
	make run_typechecker
	make run_linter
	make run_unit_test
	make run_integration_test

build:
	make install_dev
	make check_hackerrank
