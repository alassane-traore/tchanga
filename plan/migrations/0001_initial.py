# Generated by Django 4.2.3 on 2023-11-19 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('begin', models.TimeField()),
                ('end', models.TimeField()),
                ('task', models.CharField(max_length=89)),
                ('classi', models.CharField(max_length=65)),
                ('autor', models.CharField(max_length=85)),
            ],
        ),
    ]
