# Generated by Django 4.2.3 on 2023-12-22 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kasse', '0002_remove_basket_sect_remove_sector_busket_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='day',
        ),
        migrations.AddField(
            model_name='goods',
            name='s',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='goods', to='kasse.sector'),
        ),
    ]
