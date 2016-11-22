#---------------------------------------
# IMPORTS
#---------------------------------------

import os

from test   import *
from pymake import *

#---------------------------------------
# CONSTANTS
#---------------------------------------

DESTDIR = 'files2'
SRCDIR  = 'files'

#---------------------------------------
# SCRIPT
#---------------------------------------

assert_true(os.path.exists(SRCDIR), "test files missing")
assert_false(os.path.exists(DESTDIR), "temp dir should not exist yet")
assert_equal(copy(SRCDIR , DESTDIR, '*.txt'), 3, "wrong number of files copied")

test_pass()
