from celery import Celery
from celery.utils.log import get_task_logger
import time

app = Celery('one', broker="amqp://guest:guest@localhost:5672", backend="rpc://")
logger = get_task_logger(__name__)

@app.task(bind=True, default_retry_dely=30, max_retries=1)
def add(self, a, b):
    try:
        return a / b
    except ZeroDivisionError as exc:
        logger.warning("Sorry ...")
        self.retry(exc=exc, countdown=5)