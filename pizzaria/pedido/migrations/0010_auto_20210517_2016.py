# Generated by Django 3.2.2 on 2021-05-17 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0009_endereco'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='endereco',
            options={'verbose_name': 'Endereço'},
        ),
        migrations.AddField(
            model_name='pedido',
            name='endereco',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pedido.endereco'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='bairro',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
