from .models           import Todo

from django.shortcuts          import render, redirect
from django.views              import View
from django.core.files.storage import default_storage
from django.core.files.base    import ContentFile

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
            .values('id', 'title', 'image', 'is_active', 'created_at')
        )

        return render(request, 'todo/index.html', {'todo_list': todo_list})

class TodoCreateView(View):
    def post(self, request):
        title = request.POST.get('title')
        file = request.FILES.get('image')

        if file:
            image = default_storage.save(file.name, ContentFile(file.read()))
        else:
            image = None

        Todo.objects.create(
            title     = title if title else 'Untitled',
            image     = image,
            is_active = True
        )

        return redirect('/')

class TodoDeleteView(View):
    def post(self, request, todo_id):
        Todo.objects.get(id = todo_id).delete()

        return redirect('/')

class TodoStatusView(View):
    def post(self, request, todo_id):
        todo = Todo.objects.get(id = todo_id)
        todo.is_active = True if todo.is_active == False else False
        todo.save()

        return redirect('/')
