# Generated by Django 4.1 on 2023-12-11 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planszowki', '0009_remove_gra_liczba_graczy_gra_max_gracze_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='komentarz',
            name='ocena',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1, null=True),
        ),
    ]
