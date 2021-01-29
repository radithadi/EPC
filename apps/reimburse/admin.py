from django.contrib import admin
from .models import Reimburse

class ReimburseAdmin(admin.ModelAdmin):
    pass

admin.site.register(Reimburse, ReimburseAdmin)