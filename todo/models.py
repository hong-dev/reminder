from django.db import models

class Todo(models.Model):
    title      = models.CharField(max_length = 100)
    image      = models.URLField(null = True)
    is_active  = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'todos'
