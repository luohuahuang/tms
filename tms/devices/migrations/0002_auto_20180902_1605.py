# Generated by Django 2.1 on 2018-09-02 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='sn',
            field=models.CharField(default='123456', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicaldevice',
            name='sn',
            field=models.CharField(default='123456', max_length=20),
            preserve_default=False,
        ),
    ]