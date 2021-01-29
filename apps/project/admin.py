from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Customer',        {'fields': ['client']}),
        ('Description',     {'fields': ['name', 'description']}),
        ('Execution Date',  {'fields': ['start_date', 'end_date']}),
        ('Who is Work?',    {'fields': ['worker']}),
        ('Status',          {'fields': ['status']}),
    )
    list_display = ('name', 'status','workers')
    list_filter = ('name', 'status')
    readonly_fields = ('uuid',)
    search_fields = ('client', 'name', 'uuid', 'status')
    ordering = ('name',)

admin.site.register(Project, ProjectAdmin)