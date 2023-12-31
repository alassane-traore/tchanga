# Generated by Django 4.2.3 on 2023-12-23 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kasse', '0005_remove_basket_kaufliste_basket_kaufliste'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='costs',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='basket',
            name='kaufliste',
            field=models.ManyToManyField(blank=True, related_name='busket', to='kasse.goods'),
        ),
        migrations.AlterField(
            model_name='sector',
            name='budget',
            field=models.FloatField(),
        ),
    ]
