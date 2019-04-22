run_linter:
	python3 -m pipenv run pylint src tests

run_formatter:
	python3 -m pipenv run yapf -d -r -p src tests

run_test:
	python3 -m pipenv run pytest tests

run_test_with_cov:
	python3 -m pipenv run pytest tests --cov=src --cov-config .coveragerc

check_hackerrank:
	make run_linter
	make run_formatter
	make run_test

