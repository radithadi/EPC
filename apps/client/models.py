import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.company.models import Company
from .validators import validate_contact

class DepartmentChoices(models.TextChoices):
    project = 'project', _('Project')
    engineering = 'engineering', _('Engineering')
    purchasing = 'puchasing', _('Puchasing')
    accounting = 'accounting', _('Accounting')
    other = 'other', _('Other')

class Client(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    department = models.CharField(max_length=20, choices=DepartmentChoices.choices,  default=DepartmentChoices.project, verbose_name="Department")
    name = models.CharField(max_length=30, verbose_name="Username")
    contact = models.CharField(validators = [validate_contact], max_length=12, blank=True, verbose_name="Contact")
    email = models.EmailField(max_length=30,blank=True, verbose_name="Email")
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='uuid')
    publish = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'client'
        verbose_name_plural = 'clients'
        db_table = 'client'
        ordering = ['name', 'uuid']
        unique_together = [['name', 'uuid']]
        permissions = [('publish_client', 'Can publish client')]
        indexes = [
            models.Index(fields=['name', 'uuid','department','company']),
        ]
        default_related_name = 'Clients'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('client-detail', kwargs={'uuid': self.uuid})
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    
    # def __get_initial_name(self):
    #     return self.name[:1]
    
    # iname = property(__get_initial_name)