# Generated by Django 3.2.2 on 2021-05-17 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0006_pedido_cancelado'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='finalizado',
            field=models.BooleanField(default=False),
        ),
    ]
