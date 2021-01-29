from django.contrib import admin
from .models import Advance
class AdvanceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Advance, AdvanceAdmin)