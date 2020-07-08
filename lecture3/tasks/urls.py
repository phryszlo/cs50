from django.urls import path
from . import views

# avoid namespace collision with this 
app_name="tasks"
urlpatterns = [
  path("", views.index, name="index"),
  path("add", views.add, name="add")
]