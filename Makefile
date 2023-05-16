test:
	ruff .
	cd tests && pytest -v

test-v:
	cd tests && pytest -vv