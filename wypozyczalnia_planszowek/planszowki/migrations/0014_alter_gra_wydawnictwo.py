# Generated by Django 4.1 on 2023-12-14 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planszowki', '0013_remove_account_email_remove_account_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gra',
            name='wydawnictwo',
            field=models.IntegerField(choices=[(1, 'Portalgames'), (2, 'Rebel'), (3, 'Galakta'), (4, 'Luckyduckgames'), (5, 'Muduko'), (6, 'Naszaksięgarnia'), (7, 'Phalanx'), (8, 'G3'), (9, 'Trefl'), (10, 'Inne')], default=1),
        ),
    ]
