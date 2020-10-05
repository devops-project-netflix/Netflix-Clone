LINTER = flake8
SRC_DIR = source
REQ_DIR = requirements

FORCE:

prod:	tests

github:	FORCE
	echo "Just testing the make file"
	- git commit -a
	- git push origin ammar_aba450

tests:	unit test

test: FORCE
	python $(SRC_DIR)/runTests.py

unit:	FORCE
	echo "We have to write some tests!"

lint:	FORCE
	$(LINTER) $(SRC_DIR)/*.py
	- $(LINTER) $(SRC_DIR)/*/*.py

dev_env:	FORCE
	pip install -r $(REQ_DIR)/requirements-dev.txt