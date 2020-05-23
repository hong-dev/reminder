from .views import TodoListView, TodoCreateView, TodoDeleteView, TodoStatusView

from django.urls import path

urlpatterns = [
    path('', TodoListView.as_view()),
    path('new', TodoCreateView.as_view()),
    path('todo/<int:todo_id>', TodoDeleteView.as_view()),
    path('status/<int:todo_id>', TodoStatusView.as_view())
]
