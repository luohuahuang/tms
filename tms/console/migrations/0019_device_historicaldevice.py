# Generated by Django 2.1 on 2018-08-29 08:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('console', '0018_auto_20180828_1926'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('upd_date', models.DateTimeField(auto_now=True, verbose_name='date updated')),
                ('os_version', models.CharField(max_length=10)),
                ('device_platform', models.IntegerField(choices=[(0, 'Android'), (1, 'iOS'), (2, 'Others')], default=0)),
                ('device_status', models.IntegerField(choices=[(0, 'Available'), (1, 'Occupied'), (2, 'Broken'), (3, 'Returned')], default=0)),
                ('Tester', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='console.Tester')),
            ],
            options={
                'db_table': 'device_tab',
            },
        ),
        migrations.CreateModel(
            name='HistoricalDevice',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(blank=True, editable=False, verbose_name='date created')),
                ('upd_date', models.DateTimeField(blank=True, editable=False, verbose_name='date updated')),
                ('os_version', models.CharField(max_length=10)),
                ('device_platform', models.IntegerField(choices=[(0, 'Android'), (1, 'iOS'), (2, 'Others')], default=0)),
                ('device_status', models.IntegerField(choices=[(0, 'Available'), (1, 'Occupied'), (2, 'Broken'), (3, 'Returned')], default=0)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('Tester', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='console.Tester')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical device',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
