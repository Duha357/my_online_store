# Generated by Django 2.1.1 on 2018-10-17 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20181014_2323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='phone',
        ),
        migrations.AddField(
            model_name='account',
            name='age',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]
