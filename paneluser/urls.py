from django.urls import path
from .views import home

app_name = "paneluser"
urlpatterns = [
    path('', home),
]