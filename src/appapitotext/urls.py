from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path(f'{settings.URL_PATH_FUNCTION_ADD_TEXT}/', views.add_text, name='add_text'),
]
