# Generated by Django 4.1.7 on 2023-04-24 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_shippingaddress_user_alter_shopper_stripe_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopper',
            name='is_email_verified',
            field=models.BooleanField(default=False),
        ),
    ]
