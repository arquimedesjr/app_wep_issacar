# Generated by Django 3.1 on 2020-10-05 01:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_grupo', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name_plural': 'Grupo',
            },
        ),
        migrations.CreateModel(
            name='Reuniao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reuniao', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Reunião',
            },
        ),
        migrations.CreateModel(
            name='Tribo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_tribo', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name_plural': 'Tribo',
            },
        ),
        migrations.CreateModel(
            name='Relatorio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qnt', models.IntegerField()),
                ('data', models.DateField()),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.grupo')),
                ('reuniao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.reuniao')),
                ('tribo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tribo')),
            ],
            options={
                'verbose_name_plural': 'Relatorio',
            },
        ),
        migrations.CreateModel(
            name='Jovens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='profile_pics', verbose_name='Foto')),
                ('foto_base64', models.TextField()),
                ('nome', models.CharField(max_length=250, verbose_name='Nome - Ex: (Arquimedes Junior)')),
                ('telefone', models.CharField(max_length=11, verbose_name='Telefone - Ex: 11948924982')),
                ('presenca', models.CharField(choices=[('SIM', 'SIM'), ('NÃO', 'NÃO')], default='NÃO', max_length=3, verbose_name='Está na Reunião?')),
                ('data', models.DateField(auto_now_add=True)),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.grupo')),
                ('tribo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tribo')),
            ],
            options={
                'verbose_name_plural': 'Jovens',
            },
        ),
    ]
