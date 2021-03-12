from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path('', views.TopicListView.as_view(), name='top'),
]