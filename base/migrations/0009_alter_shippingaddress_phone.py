# Generated by Django 5.1.2 on 2025-01-22 08:14

import base.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0008_alter_orderitem_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shippingaddress",
            name="phone",
            field=models.CharField(
                blank=True,
                max_length=15,
                null=True,
                validators=[base.models.validate_phone],
            ),
        ),
    ]
