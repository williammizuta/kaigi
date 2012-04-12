import os

import tornado
try:
    os.symlink(os.path.dirname(tornado.__file__), 'tornado')
except OSError, e:
    print "Could not create link to tornado"

import wtforms
try:
    os.symlink(os.path.dirname(wtforms.__file__), 'wtforms')
except OSError, e:
    print "Could not create link to wtforms"

import mockito
try:
    os.symlink(os.path.dirname(mockito.__file__), 'mockito')
except OSError, e:
    print "Could not create link to mockito"
