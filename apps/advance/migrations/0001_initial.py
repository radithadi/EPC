# Generated by Django 3.1.5 on 2021-01-29 12:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='uuid')),
                ('category', models.CharField(choices=[('transport', 'Transport'), ('hotel', 'Hotel'), ('meal', 'Meal'), ('other', 'Other')], default='transport', max_length=30, verbose_name='Category')),
                ('description', models.TextField(verbose_name='Description')),
                ('date', models.DateField(verbose_name='Date')),
                ('ammount', models.CharField(max_length=9, verbose_name='Ammount')),
                ('status', models.CharField(choices=[('open', 'Open'), ('approve', 'Approve'), ('close', 'Close')], default='open', max_length=15, verbose_name='Status')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('approve_date', models.DateTimeField(blank=True, null=True, verbose_name='Approve Date')),
                ('approve_by', models.CharField(blank=True, max_length=50, verbose_name='Approve By')),
                ('approve_note', models.TextField(blank=True, verbose_name='Approve Note')),
                ('close_date', models.DateTimeField(blank=True, null=True, verbose_name='Close Date')),
                ('close_by', models.CharField(blank=True, max_length=50, verbose_name='Close By')),
                ('close_note', models.TextField(blank=True, verbose_name='Close Note')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Advances', to='project.project', verbose_name='Projects')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Advances', to=settings.AUTH_USER_MODEL, verbose_name='Users')),
            ],
            options={
                'verbose_name': 'advance',
                'verbose_name_plural': 'advances',
                'db_table': 'advance',
                'ordering': ['project', 'user', 'name', 'category', 'status', 'date'],
                'permissions': [('approve_advance', 'Can approve advance'), ('close_advance', 'Can close advance')],
                'default_related_name': 'Advances',
            },
        ),
        migrations.AddIndex(
            model_name='advance',
            index=models.Index(fields=['project', 'user', 'name', 'uuid', 'category', 'status', 'date'], name='advance_project_a45020_idx'),
        ),
    ]
