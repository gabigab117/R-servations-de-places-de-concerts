# Generated by Django 4.1.7 on 2023-04-07 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_cart_order_validated'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='stripe_id',
            field=models.CharField(blank=True, max_length=90),
        ),
    ]
