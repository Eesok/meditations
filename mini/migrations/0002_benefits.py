# Generated by Django 3.1.1 on 2020-09-02 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mini', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Benefits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('benefit', models.CharField(max_length=100)),
                ('practice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='benefits', to='mini.meditation')),
            ],
        ),
    ]
