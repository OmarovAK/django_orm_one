from django.contrib import admin

from library.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'date_pub']
    list_filter = ['author',]
    ordering = ['name']
