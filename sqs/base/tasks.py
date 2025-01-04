from celery import shared_task


@shared_task(bind=True)
def somar(self):
    return 1 + 2
