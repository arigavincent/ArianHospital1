"""
WSGI config for Arian project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import sys

# Add project directories to the Python path
sys.path.append('/home/Anita/ArianHospital1')       # outer folder
sys.path.append('/home/Anita/ArianHospital1/Arian') # inner folder containing settings.py

# Activate your virtualenv
activate_this = '/home/Anita/venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# Set the settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Arian.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
