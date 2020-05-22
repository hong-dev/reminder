from .views import TodoListView

from django.urls import path

urlpatterns = [
    path('', TodoListView.as_view())
]
