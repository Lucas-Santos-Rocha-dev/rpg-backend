# Generated by Django 4.2.4 on 2023-09-08 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aventura', '0001_initial'),
        ('mightyblade', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='aventura',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categorias_da_aventura', to='aventura.aventura'),
        ),
    ]
