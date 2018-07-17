python_home = '/home/nagios/nagiosapi'

activate_this = python_home + '/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import os
import sys

APP_HOME = "/var/www/nagiosapi/nagios"
sys.path.append(APP_HOME)
from rest import app as application
