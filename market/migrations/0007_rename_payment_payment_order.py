# Generated by Django 4.1.5 on 2023-02-18 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0006_car_price_payment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='payment',
            new_name='order',
        ),
    ]
