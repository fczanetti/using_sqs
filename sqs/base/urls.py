from django.urls import path
from sqs.base import views


app_name = "base"
urlpatterns = [
    path("register/", views.register, name="register")
]