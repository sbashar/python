run_linter:
	ruff check src tests

run_formatter:
	ruff format src tests

run_test:
	pytest tests

run_test_with_cov:
	pytest tests --cov=src

check_all:
	make run_linter
	make run_formatter
	make run_test_with_cov
