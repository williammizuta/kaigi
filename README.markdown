# Requirements
* python2.7
* python-virtualenv
* make

# Install
* type `virtualenv --python=python2.7 --no-site-packages kaigi-python`
* type `cat requirements.txt | xargs kaigi-python/bin/pip install`

# Running the server
* load your virtualenv: `source kaigi-python/bin/activate`
* type `make`
* access http://localhost:8080/ in a browser

# Running the tests
* load your virtualenv: `source kaigi-python/bin/activate`
* type `make test`
