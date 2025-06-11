from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("work_experiences/", views.work_experiences, name="work_experiences"),
    path("education/", views.education, name="education"),
    path("contact/", views.contact, name="contact"),
]
