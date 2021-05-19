# Generated by Django 3.2.2 on 2021-05-19 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0010_auto_20210517_2016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='cancelado',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='confirmado',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='entregue',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='finalizado',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='saiu_para_entrega',
        ),
        migrations.AddField(
            model_name='pedido',
            name='status',
            field=models.CharField(choices=[('AGUARDANDO_CONFIRMACAO', 'Aguardando Confirmação'), ('CONFIRMADO', 'Confirmado'), ('FINALIZADO', 'Finalizado'), ('SAIU_PARA_ENTREGA', 'Saiu Para Entrega'), ('ENTREGUE', 'Entregue')], default='AGUARDANDO_CONFIRMACAO', max_length=60),
        ),
    ]
