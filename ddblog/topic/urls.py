from django.urls import path

from . import views

urlpatterns = [
    #http://1270.0.1:8000/v1/topic/tedu
    path('<str:author_id>',views.TopicViews.as_view())
]