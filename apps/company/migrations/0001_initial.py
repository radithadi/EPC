# Generated by Django 3.1.5 on 2021-01-29 12:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('address', models.TextField(blank=True, verbose_name='Address')),
                ('city', models.CharField(max_length=20, verbose_name='City')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='UUID')),
                ('publish', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'company',
                'verbose_name_plural': 'companies',
                'db_table': 'company',
                'ordering': ['name', 'uuid'],
                'permissions': [('pubish_company', 'Can publish company')],
                'default_related_name': 'Companies',
            },
        ),
        migrations.AddIndex(
            model_name='company',
            index=models.Index(fields=['name', 'uuid'], name='company_name_a4a966_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='company',
            unique_together={('name', 'uuid')},
        ),
    ]
