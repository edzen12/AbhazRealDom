from __future__ import absolute_import, unicode_literals

from celery import Celery

import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'abhaz.settings')


app = Celery('abhaz')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {!r}'.format(self.request))