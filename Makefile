full-install:
	python3 -m venv .venv
	.venv/bin/python3 --version
	.venv/bin/python3 -m pip install --upgrade pip
	.venv/bin/python3 -m pip install -r requirements/base.txt

dev-install:
	.venv/bin/python3 -m pip install -r requirements/dev.txt
	.venv/bin/python3 -m pip install -e .

install:
	pip install --upgrade pip
	pip install -r requirements/base.txt

dev-migrations:
	alembic init migrations   # Configure alembic.ini avec sqlalchemy.url = sqlite:///./rag.db
	alembic revision --autogenerate -m "init db"
	alembic upgrade head

migrations:
	alembic revision --autogenerate -m "init"
	alembic upgrade head

migrate:
	alembic upgrade head

test:
	pytest tests

run:
	uvicorn percefon.main:app --host "0.0.0.0" --port 8000 --reload

pep8:
	# Don't remove their commented follwing command lines:
	# autopep8 --in-place --aggressive --aggressive --recursive .
	# autopep8 --in-place --aggressive --aggressive example.py
