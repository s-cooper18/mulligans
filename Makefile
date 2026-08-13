test:
	python3 -m pytest tests

lint:
	ruff format .
	ruff check .

install:
	python3 -m pip install .