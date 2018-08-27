# Generated by Django 2.1 on 2018-08-26 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('console', '0009_auto_20180826_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='release',
            name='release_platform',
            field=models.IntegerField(choices=[(1, 'Generic'), (2, 'Android'), (3, 'iOS'), (4, 'Web'), (5, 'Others')], default=1),
        ),
    ]