# Generated by Django 4.1 on 2023-11-19 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planszowki', '0003_alter_gra_max_gracze_alter_gra_min_gracze'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gra',
            name='max_gracze',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '134'), (14, '15')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='gra',
            name='min_gracze',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], default=1, null=True),
        ),
    ]
