mongodb-install:
	sh scripts/mongodb-setup.sh

init:
	python3 -m pip install -r requirements.txt

test:
	python3 -m pytest ./tests

