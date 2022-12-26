from celery import Celery

import json
import os
from dotenv import load_dotenv

load_dotenv()

BROKER_URL = os.getenv('BROKER_URL')
BACKEND_URL = os.getenv('BACKEND_URL')

print("BACKEND_URL: ",BROKER_URL)

celery = Celery('task',
    broker=BROKER_URL,
    backend=BACKEND_URL
)

celery.autodiscover_tasks(packages=['demo.task'])
print("All tasks: ")
print(celery.tasks.keys())