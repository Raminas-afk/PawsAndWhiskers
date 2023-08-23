web: gunicorn pawsandwhiskers.wsgi
worker: celery -A pawsandwhiskers worker -l info
beat: celery -A pawsandwhiskers beat -l info

