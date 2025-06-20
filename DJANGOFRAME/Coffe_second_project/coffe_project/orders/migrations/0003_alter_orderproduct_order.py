# Generated by Django 5.2.1 on 2025-05-29 20:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0002_order_order_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderproduct",
            name="order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="order_products",
                to="orders.order",
            ),
        ),
    ]
