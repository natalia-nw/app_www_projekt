# Generated by Django 4.1 on 2023-11-19 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planszowki', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wypozyczenie',
            old_name='tytul',
            new_name='gra',
        ),
    ]