# Generated by Django 4.1.7 on 2023-04-13 20:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_shopper_stripe_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to=settings.AUTH_USER_MODEL, verbose_name='utilisateur'),
        ),
        migrations.AlterField(
            model_name='shopper',
            name='stripe_id',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
