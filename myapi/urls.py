

from django.urls import path

from .views import get_answer
app_name = 'myapi'

urlpatterns = [
    path('get_answer/', get_answer, name='myapi'),
   
]