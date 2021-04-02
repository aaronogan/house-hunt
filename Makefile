mongodb-install:
	sh scripts/mongodb-setup.sh

init:
	python3 -m pip install -r requirements.txt

test:
	python3 -m pytest ./tests

venv:
	source venv/bin/activate

viewer:
	python3 viewer.py

