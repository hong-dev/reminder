from .models import Todo

from django.shortcuts import render
from django.views     import View

class TodoListView(View):
    def get(self, request):
        status = request.GET.get('status')

        filter_condition = {}
        if status == 'active':
            filter_condition['is_active'] = True
        elif status == 'done':
            filter_condition['is_active'] = False

        todo_list = (
            Todo
            .objects
            .filter(**filter_condition)
            .order_by('created_at')
            .values('title', 'image', 'is_active', 'created_at')
        )

        return render(request, 'todo/index.html', {'todo_list': list(todo_list)})
