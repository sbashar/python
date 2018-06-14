pre_commit_check_hackerrank:
	cd components/hackerrank && make check_hackerrank

pre_commit_check_codewars:
	cd components/codewars && make check_codewars

pre_commit_check_practice:
	cd components/codewars && make check_practice

pre_commit_check_all:
	make pre_commit_check_hackerrank
	make pre_commit_check_codewars
	make pre_commit_check_practice

build_hackerrank:
	cd components/hackerrank && make build

build_codewars:
	cd components/codewars && make build

build_codewars:
	cd components/practice && make build

build_all:
	make build_practice
	make build_hackerrank
	make build_codewars
