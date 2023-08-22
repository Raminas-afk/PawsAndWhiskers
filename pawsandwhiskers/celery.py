from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pawsandwhiskers.settings')

app = Celery('main')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'send-daily-emails': {
        'task': 'main.tasks.send_daily_email_task',
        'schedule': crontab(hour=12, minute=0),
    },
}

# test change for heroku
