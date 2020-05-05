import os
os.environ.setdefault('DJANGO_SETTING_MODULE', 'test_project.settings')

import django
django.setup()

import random
from test_app.models import