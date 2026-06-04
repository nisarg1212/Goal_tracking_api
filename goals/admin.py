from django.contrib import admin
from .models import Goals

class GoalAdmin(admin.ModelAdmin):
    model = Goals
    list_display = ['title', 'description','user','created_at','updated_at']

    search_fields = ['title','description']

admin.site.register(Goals,GoalAdmin)