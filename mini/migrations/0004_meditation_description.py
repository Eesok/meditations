# Generated by Django 3.1.1 on 2020-09-02 16:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mini', '0003_auto_20200902_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='meditation',
            name='description',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
