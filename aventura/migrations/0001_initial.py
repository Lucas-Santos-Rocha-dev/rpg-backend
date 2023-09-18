# Generated by Django 4.2.4 on 2023-09-08 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoAventura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('alterado_em', models.DateTimeField(auto_now=True, verbose_name='Alterado em')),
                ('nome', models.CharField(max_length=160, verbose_name='Nome')),
                ('descricao', models.TextField(blank=True)),
                ('sistema_utilizado', models.CharField(choices=[('MIGHTYBLADE', 'Mightyblade'), ('NARUTO', 'Naruto')], default='MIGHTYBLADE', max_length=50, verbose_name='Sistema utilizado')),
            ],
            options={
                'verbose_name': 'TipoAventura',
                'verbose_name_plural': 'TipoAventuras',
            },
        ),
        migrations.CreateModel(
            name='Aventura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('alterado_em', models.DateTimeField(auto_now=True, verbose_name='Alterado em')),
                ('nome', models.CharField(max_length=160, verbose_name='Nome')),
                ('descricao', models.TextField(blank=True)),
                ('mestre', models.CharField(max_length=160, verbose_name='Nome da aventura')),
                ('tipo_aventura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aventuras_do_tipo', to='aventura.tipoaventura')),
            ],
            options={
                'verbose_name': 'Aventura',
                'verbose_name_plural': 'Aventuras',
            },
        ),
    ]
