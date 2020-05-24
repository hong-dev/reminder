from .views import (
    TodoListView,
    TodoCreateView,
    TodoDeleteView,
    TodoStatusView
)

from django.urls import path
from django.conf.urls.static import static
from reminder import settings

urlpatterns = [
    path('', TodoListView.as_view()),
    path('new', TodoCreateView.as_view()),
    path('todo/<int:todo_id>', TodoDeleteView.as_view()),
    path('status/<int:todo_id>', TodoStatusView.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
