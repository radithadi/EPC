from django.contrib import admin
from .models import Timesheet
from .forms import TimesheetForm
from datetime import date

class TimesheetAdmin(admin.ModelAdmin):
    pass

admin.site.register(Timesheet, TimesheetAdmin)