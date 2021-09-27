# """
# WSGI config for Grocery_Bag project.

# It exposes the WSGI callable as a module-level variable named ``application``.

# For more information on this file, see
# https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
# """

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Grocery_Bag.settings')

# application = get_wsgi_application()


# This file contains the WSGI configuration required to serve up your
# web application at http://saurav.pythonanywhere.com/
# It works by setting the variable 'application' to a WSGI handler of some
# description.
#
# The below has been auto-generated for your Django project

from django.core.wsgi import get_wsgi_application
import os
import sys

# add your project directory to the sys.path
project_home = '/home/saurav/Grocery_Bag'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# set environment variable to tell django where your settings.py is
os.environ['DJANGO_SETTINGS_MODULE'] = 'Grocery_Bag.settings'


# serve django via WSGI
application = get_wsgi_application()
