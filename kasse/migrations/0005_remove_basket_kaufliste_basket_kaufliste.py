# Generated by Django 4.2.3 on 2023-12-22 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kasse', '0004_remove_basket_day_remove_goods_d'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='kaufliste',
        ),
        migrations.AddField(
            model_name='basket',
            name='kaufliste',
            field=models.ManyToManyField(blank=True, null=True, related_name='busket', to='kasse.goods'),
        ),
    ]