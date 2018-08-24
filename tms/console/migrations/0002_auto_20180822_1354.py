# Generated by Django 2.1 on 2018-08-22 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('console', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testcase',
            name='test_case_tier',
            field=models.IntegerField(choices=[(1, 'tier 1'), (2, 'tier 2'), (3, 'tier 3'), (2, 'tier 4'), (3, 'tier 5')], default=1),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='test_case_type',
            field=models.IntegerField(choices=[(1, 'Functional'), (2, 'Acceptance'), (3, 'Accessibility'), (4, 'Automated'), (5, 'Compatibility'), (6, 'Performance'), (7, 'Regression'), (8, 'Security'), (9, 'Sanity'), (10, 'Usability'), (11, 'Localization')]),
        ),
    ]
