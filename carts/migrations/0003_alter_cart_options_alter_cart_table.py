# Generated by Django 5.0.6 on 2024-07-08 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_cart_session_key_alter_cart_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': 'Cart', 'verbose_name_plural': 'Carts'},
        ),
        migrations.AlterModelTable(
            name='cart',
            table='cart',
        ),
    ]
