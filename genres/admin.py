from django.contrib import admin
from .models import Genre

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ["name", ]
    prepopulated_fields = {"slug": ("name",)}
    
