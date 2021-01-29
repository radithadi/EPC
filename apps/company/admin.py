from django.contrib import admin
from .models import Company
from apps.client.models import Client

class ChoiceInline(admin.StackedInline):
    model = Client
    extra = 0
    max_num = 10

class CompanyAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Customer Company', {
            'fields': (
                'name',
                'address',
                'city',
                'uuid',
            ),
        }),
    )
    list_display = ('name', 'city',)
    list_filter = ('city',)
    inlines = [
        ChoiceInline,
    ]
    readonly_fields = ('uuid',)
    search_fields = ('name', 'city')
    ordering = ('name', 'city')

admin.site.register(Company, CompanyAdmin)
