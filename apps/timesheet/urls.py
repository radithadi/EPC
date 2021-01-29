from django.urls import path
from .views import TimesheetCreateView, TimesheetUpdateView, TimesheetListView

app_name = 'timesheet'

urlpatterns = [
    path('', TimesheetListView.as_view(), name='timesheet'),
    path('timesheet-create/', TimesheetCreateView.as_view(), name='timesheet-create'),
    path('timesheet-update/<uuid:uuid>', TimesheetUpdateView.as_view(), name='timesheet-update'),
]