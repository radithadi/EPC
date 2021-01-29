import uuid
from django.db import models
from django.contrib.auth import get_user_model
from apps.project.models import Project
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class ReimburseChoices(models.TextChoices):
    transport   = 'transport',_('Transport')
    hotel       = 'hotel',_('Hotel')
    meal        = 'meal',_('Meal')
    other       = 'other',_('Other')

class StatusChoices(models.TextChoices):
    open    = 'open',_('Open')
    approve = 'approve',_('Approve')
    close   = 'close',_("Close")

class Reimburse(models.Model):    
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Projects')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name="Users")
    name = models.CharField(max_length=50, verbose_name='Name')
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Code')
    category = models.CharField(max_length=30, choices=ReimburseChoices.choices, default=ReimburseChoices.transport, verbose_name='Category')
    description = models.TextField(verbose_name='Description')
    date = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Date')
    ammount = models.CharField(max_length=9, verbose_name='Ammount')
    status = models.CharField(max_length=15, choices=StatusChoices.choices, default=StatusChoices.open, verbose_name='Status')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Created Date')
    approve_date = models.DateTimeField(blank=True, null=True, auto_now=False, auto_now_add=False, verbose_name='Approve Date')
    approve_by = models.CharField(blank=True, max_length=50, verbose_name='Approve By')
    approve_note = models.TextField(blank=True, verbose_name='Approve Note')
    close_date = models.DateTimeField(blank=True, null=True, auto_now=False, auto_now_add=False, verbose_name='Close Date')
    close_by = models.CharField(blank=True, max_length=50, verbose_name='Close By')
    close_note = models.TextField(blank=True, verbose_name='Close Note')

    class Meta:
        verbose_name = 'reimburse'
        verbose_name_plural = 'reimburses'
        db_table = 'reimburse'
        ordering = ['project', 'user', 'name', 'category', 'status', 'date']
        permissions = [('approve_reimburse', 'Can approve reimburse'), ('close_reimburse', 'Can close reimburse'), ]
        indexes = [
            models.Index(fields=['project', 'user', 'name', 'uuid',  'category', 'status', 'date',]),
        ]
        default_related_name = 'Reimburses'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.status == 'approve' and not self.approve_date:
            self.approve_date = timezone.now()
        elif self.status == 'close' and not self.close_date:
            if not self.approve_date:
                self.approve_date = timezone.now()
            self.close_date = timezone.now()
        super().save(*args, **kwargs)

