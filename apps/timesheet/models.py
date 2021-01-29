import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from apps.project.models import Project
# from .validators import validate_date

class TimesheetChoices(models.TextChoices):
    work        = 'work', _('Work')
    leave       = 'leave', _('Leave')
    sick        = 'sick',_('Sick')
    learning    = 'learning',_('Learning')
    Sales       = 'sales support', _('Sales Support')
    office      = 'office administrations',_('Office Administrations')
    holiday     = 'holiday',_('Holiday')
    other       = 'other',_('Other')

class Timesheet(models.Model):        
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Project')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Users')
    date = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Date')
    activity = models.CharField(choices=TimesheetChoices.choices, default=TimesheetChoices.work, max_length=30, verbose_name='Activity')
    description = models.TextField(verbose_name='Description')
    location = models.CharField(max_length=50, verbose_name='location')
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='UUID')
    
    class Meta:
        verbose_name = 'timesheet'
        verbose_name_plural = 'timesheets'
        db_table = 'timesheet'
        ordering = ['project', 'user', 'date', 'activity']
        indexes = [
            models.Index(fields=['project', 'user', 'date', 'uuid', 'activity']),
        ]
        unique_together = ['user', 'date']
        default_related_name = 'Timesheets'

    def __str__(self):
        return str(self.user) + ': ' + str(self.date)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

