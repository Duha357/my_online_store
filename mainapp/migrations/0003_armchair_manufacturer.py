# Generated by Django 2.1.1 on 2018-10-07 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20181007_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='armchair',
            name='Manufacturer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mainapp.Manufacturer'),
            preserve_default=False,
        ),
    ]