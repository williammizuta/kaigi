GAE_SDK=../google_appengine

run: setup
	python $(GAE_SDK)/dev_appserver.py .

test: setup
	nosetests --with-gae --gae-lib-root=$(GAE_SDK) -i test -i should test

setup:
	bash ../kaigi-python/bin/activate

.PHONY: setup test run
