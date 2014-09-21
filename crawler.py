# This is the Crawler App

import sys
import os

DEBUG = os.environ.get('DEBUG', False)

#print sys.path
#print os.get_cwd()

if DEBUG:
    print sys.path
    print os.get_cwd()

def crawler():
    pass
