GAE_SDK=../google_appengine

run: prepare
	python $(GAE_SDK)/dev_appserver.py .

test: prepare
	nosetests --with-gae --gae-lib-root=$(GAE_SDK) -i test -i should test

prepare:
	python link_libraries.py

deploy:
	rm mockito
	python $(GAE_SDK)/appcfg.py update .

.PHONY: prepare test run deploy
