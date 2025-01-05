from celery import shared_task
from .models import Register


@shared_task(bind=True)
def register(self, data: dict):
    name = data["name"]
    phone = data["phone"]
    address = data["address"]

    Register.objects.create(name=name, phone=phone, address=address)
