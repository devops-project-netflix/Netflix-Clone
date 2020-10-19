LINTER = flake8
SRC_DIR = source
REQ_DIR = requirements

FORCE:

prod:	tests github

github:	FORCE
	echo "Committing the changes to github"
	- git commit -a
	- git push origin master

tests:	lint unit
		
test: FORCE
	 -python $(SRC_DIR)/runTests.py

unit:	FORCE
	echo "We have to write some tests!"

lint:	FORCE
	$(LINTER) $(SRC_DIR)/*/*.py

dev_env:	FORCE
	pip install -r $(REQ_DIR)/requirements-dev.txt

runprod: FORCE
	cd source; ./local.sh

