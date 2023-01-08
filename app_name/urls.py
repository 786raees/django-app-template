from django.urls import path
from . import views as {{ app_name }}_views

app_name = "{{ app_name }}"

urlpatterns = [
    # path("", {{ app_name }}_views.home, name="home")
]
