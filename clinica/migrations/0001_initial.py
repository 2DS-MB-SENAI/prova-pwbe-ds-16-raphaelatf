# Generated by Django 4.2 on 2025-04-08 12:00

import clinica.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('especialidade', models.CharField(choices=[('clinico', 'Clínico Geral'), ('cardiologia', 'Cardiologia'), ('neurologia', 'Neurologia'), ('ortopedia', 'Ortopedia'), ('psicologia', 'Psicologia'), ('pediatria', 'Pediatria')], max_length=50)),
                ('crm', models.CharField(max_length=10, unique=True, validators=[clinica.models.validar_crm])),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paciente', models.CharField(max_length=100)),
                ('data', models.DateTimeField(validators=[clinica.models.validar_data_futura])),
                ('status', models.CharField(choices=[('agendado', 'Agendado'), ('realizado', 'Realizado'), ('cancelado', 'Cancelado')], default='agendado', max_length=10)),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinica.medico')),
            ],
        ),
    ]
