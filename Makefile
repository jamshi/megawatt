# Some simple testing tasks (sorry, UNIX only).

FLAGS=


flake:
	pyflakes web
	pep8 web

test:
	python manage.py test
	
clean:
	rm -rf `find . -name __pycache__`
	rm -rf `find . -name .pytest_cache`
	rm -rf `find . -name .tox`
	rm -rf `find . -name '*.egg-info' `
	rm -f `find . -type f -name '*.py[co]' `
	rm -f `find . -type f -name '*~' `
	rm -f `find . -type f -name '.*~' `
	rm -f `find . -type f -name '@*' `
	rm -f `find . -type f -name '#*#' `
	rm -f `find . -type f -name '*.orig' `
	rm -f `find . -type f -name '*.rej' `
	rm -f .coverage
	rm -rf coverage
	rm -rf build
	rm -rf htmlcov
	rm -rf dist

.PHONY: flake clean test
