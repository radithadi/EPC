import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from apps.client.models import Client
from django.core.exceptions import ValidationError

class ProjectChoices(models.TextChoices):
    open = 'open', _('Open')
    close = 'close', _('Close')

class Project(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Client")
    name = models.CharField(max_length=50, unique=True, verbose_name="Name")
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, verbose_name="Code")
    start_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name="Start Date")
    end_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name="End Date")
    description = models.TextField(blank=True, verbose_name="Description")
    worker = models.ManyToManyField(get_user_model(), verbose_name="Workers")
    status = models.CharField(max_length=15, choices=ProjectChoices.choices, default=ProjectChoices.open, verbose_name="Status")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'project'
        verbose_name_plural = 'projects'
        db_table = 'project'
        ordering = ['client', 'name',  'uuid']
        unique_together = [['name', 'uuid']]
        permissions = [('close_poject', 'Can close project')]
        indexes = [
            models.Index(fields=['client', 'name', 'uuid']),
        ]
        default_related_name = 'Projects'

    def __str__(self):
        return self.name
    
    # def clean(self):
    #     if self.start_date < self.end_date:
    #         raise ValidationError({
    #                 'start_date': ValidationError(_('Please correct date input.'), code='invalid'),
    #                 'end_date': ValidationError(_('Please correct date input'), code='invalid'),
    #         })
    

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
    def __get_worker(self):
        return ",".join([str(p) for p in self.worker.all()])
    
    workers = property(__get_worker)