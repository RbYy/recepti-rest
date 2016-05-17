import os
from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'svincnik.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "svincnik.settings")

import django
application = get_wsgi_application()
#import p

