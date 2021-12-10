# Generated by Django 3.2.7 on 2021-10-27 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('iduser', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30)),
                ('passworduser', models.CharField(max_length=30)),
                ('rol', models.CharField(choices=[('ADMIN', 'ADMIN'), ('BODEGA', 'BODEGA'), ('FINANZAS', 'FINANZAS'), ('COCINA', 'COCINA')], default='ADMIN', max_length=30)),
                ('state', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'Login',
            },
        ),
    ]
