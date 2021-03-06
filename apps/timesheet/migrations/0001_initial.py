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
            name='Timesheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date')),
                ('activity', models.CharField(choices=[('work', 'Work'), ('leave', 'Leave'), ('sick', 'Sick'), ('learning', 'Learning'), ('sales support', 'Sales Support'), ('office administrations', 'Office Administrations'), ('holiday', 'Holiday'), ('other', 'Other')], default='work', max_length=30, verbose_name='Activity')),
                ('description', models.TextField(verbose_name='Description')),
                ('location', models.CharField(max_length=50, verbose_name='location')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='UUID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Timesheets', to='project.project', verbose_name='Project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Timesheets', to=settings.AUTH_USER_MODEL, verbose_name='Users')),
            ],
            options={
                'verbose_name': 'timesheet',
                'verbose_name_plural': 'timesheets',
                'db_table': 'timesheet',
                'ordering': ['project', 'user', 'date', 'activity'],
                'default_related_name': 'Timesheets',
            },
        ),
        migrations.AddIndex(
            model_name='timesheet',
            index=models.Index(fields=['project', 'user', 'date', 'uuid', 'activity'], name='timesheet_project_d035da_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='timesheet',
            unique_together={('user', 'date')},
        ),
    ]
