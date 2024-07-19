from django.contrib import admin
from quickstart.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'content', 'created_at', 'updated_at')

    def content(self, obj):
        if len(obj.body) > 10:
            return f'{obj.body[:10]}...'
