GAE_SDK=../google_appengine

run:
	python $(GAE_SDK)/dev_appserver.py .

test:
	nosetests --with-gae --gae-lib-root=$(GAE_SDK) -i test -i should test

.PHONY: setup test run
