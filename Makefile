run_linter:
	pipenv run pylint src tests

run_formatter:
	pipenv run yapf -d -r -p src tests

run_test:
	pipenv run pytest tests

run_test_with_cov:
	pipenv run pytest tests --cov=src

check_all:
	make run_linter
	make run_formatter
	make run_test_with_cov
