.PHONY: black-check
black-check:
	poetry run black --check src scripts tests app.py stack.py

.PHONY: black
black:
	poetry run black src scripts tests app.py stack.py

.PHONY: flake8
flake8:
	poetry run flake8 src scripts tests app.py stack.py

.PHONY: isort-check
isort-check:
	poetry run isort --check-only src scripts tests app.py stack.py

.PHONY: isort
isort:
	poetry run isort src scripts tests app.py stack.py

.PHONY: mdformat
mdformat:
	poetry run mdformat *.md

.PHONY: mdformat-check
mdformat-check:
	poetry run mdformat --check *.md

.PHONY: mypy
mypy:
	poetry run mypy src scripts app.py stack.py

.PHONY: test
test:
	poetry run pytest tests --cov=src --cov-report term-missing --durations 5

.PHONY: format
format:
	$(MAKE) black
	$(MAKE) isort
	$(MAKE) mdformat

.PHONY: lint
lint:
	$(MAKE) black-check
	$(MAKE) isort-check
	$(MAKE) mdformat-check
	$(MAKE) flake8
	$(MAKE) mypy

.PHONY: test-all
test-all:
	$(MAKE) lint
	$(MAKE) test