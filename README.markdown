# Requirements
* python2.5
* python-virtualenv

# Install
* `virtualenv --python=python2.5 --no-site-packages kaigi-python`
* `cat requirements.txt | xargs kaigi-python/bin/pip install`

# Running the server
* load your virtualenv: `source kaigi-python/bin/activate`
* type `python <path to your google appengine>/dev_appserver.py <path to your kaigi project>
* access http://localhost:8080/ in a browser
