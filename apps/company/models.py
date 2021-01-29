import uuid
from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=30, verbose_name="Name")
    address = models.TextField(blank=True, verbose_name="Address")
    city = models.CharField(max_length=20, verbose_name="City")
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='UUID')
    publish = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'company'
        verbose_name_plural = 'companies'
        db_table = 'company'
        ordering = ['name', 'uuid']
        unique_together = [['name', 'uuid']]
        permissions = [('pubish_company', 'Can publish company')]
        indexes = [
            models.Index(fields=['name', 'uuid']),
        ]
        default_related_name = 'Companies'

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
    # def __get_initial_name(self):
    #     return self.name[:1]
    
    # iname = property(__get_initial_name)
