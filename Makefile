pre_commit_check_hackerrank:
	cd hackerrank && make check_hackerrank

pre_commit_check_all:
	make pre_commit_check_hackerrank

