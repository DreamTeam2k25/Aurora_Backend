import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('core')

app.conf.broker_url = 'amqp://anthony:anthony321@localhost:5672//'

app.conf.broker_connection_retry_on_startup = True

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.task_acks_late = True  
app.conf.task_reject_on_worker_lost = True  
app.conf.task_default_queue = 'emails'  

@app.task(bind=True)
def debug_task(self):
    print(f"Task executada: {self.request!r}")
