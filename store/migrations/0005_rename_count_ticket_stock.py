# Generated by Django 4.1.7 on 2023-04-20 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_remove_cart_order_validated'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='count',
            new_name='stock',
        ),
    ]