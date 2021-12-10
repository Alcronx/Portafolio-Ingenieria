# Generated by Django 3.2.7 on 2021-10-27 02:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('BodegaApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('clientid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('members', models.IntegerField()),
                ('state', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'Client',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('menuid', models.AutoField(primary_key=True, serialize=False)),
                ('recipe', models.CharField(max_length=1000)),
                ('cookingtime', models.DateField()),
                ('menucost', models.BigIntegerField(blank=True, null=True)),
                ('menuprice', models.BigIntegerField()),
                ('state', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'Menu',
            },
        ),
        migrations.CreateModel(
            name='Orderclient',
            fields=[
                ('ordeclientid', models.AutoField(primary_key=True, serialize=False)),
                ('orderhour', models.DateField()),
                ('orderdate', models.DateField()),
                ('orderclienttotal', models.BigIntegerField(blank=True, null=True)),
                ('state', models.CharField(max_length=1)),
                ('client_clientid', models.ForeignKey(db_column='client_clientid', on_delete=django.db.models.deletion.CASCADE, to='RestaurantApp.client')),
            ],
            options={
                'db_table': 'Orderclient',
            },
        ),
        migrations.CreateModel(
            name='RestaurantTable',
            fields=[
                ('tableid', models.AutoField(primary_key=True, serialize=False)),
                ('tableNumber', models.IntegerField()),
                ('tableMembers', models.IntegerField()),
                ('aviable', models.CharField(choices=[('1', 'DISPONIBLE'), ('0', 'NO DISPONIBLE')], default='DISPONIBLE', max_length=1)),
                ('state', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'RestaurantTable',
            },
        ),
        migrations.CreateModel(
            name='Waiter',
            fields=[
                ('waiterid', models.AutoField(primary_key=True, serialize=False)),
                ('rut', models.CharField(max_length=10)),
                ('name1', models.CharField(max_length=50)),
                ('name2', models.CharField(max_length=50)),
                ('lastname1', models.CharField(max_length=50)),
                ('lastname2', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'waiter',
            },
        ),
        migrations.CreateModel(
            name='Reserved',
            fields=[
                ('reserveid', models.AutoField(primary_key=True, serialize=False)),
                ('reservedate', models.DateField()),
                ('reservehour', models.DateField()),
                ('state', models.CharField(max_length=1)),
                ('rt_tableid', models.ForeignKey(db_column='rt_tableid', on_delete=django.db.models.deletion.CASCADE, to='RestaurantApp.restauranttable')),
            ],
            options={
                'db_table': 'Reserved',
            },
        ),
        migrations.CreateModel(
            name='Productmenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('total', models.BigIntegerField()),
                ('pmmenuid', models.ForeignKey(db_column='pmmenuid', on_delete=django.db.models.deletion.CASCADE, to='RestaurantApp.menu')),
                ('pmproductid', models.ForeignKey(db_column='pmproductid', on_delete=django.db.models.deletion.CASCADE, to='BodegaApp.product')),
            ],
            options={
                'db_table': 'ProductMenu',
                'unique_together': {('pmmenuid', 'pmproductid')},
            },
        ),
        migrations.CreateModel(
            name='Orderclientdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiantity', models.IntegerField()),
                ('total', models.BigIntegerField()),
                ('ocdmenuid', models.ForeignKey(db_column='ocdmenuid', on_delete=django.db.models.deletion.CASCADE, to='RestaurantApp.menu')),
                ('ocdorderclientid', models.ForeignKey(db_column='ocdorderclientid', on_delete=django.db.models.deletion.CASCADE, to='RestaurantApp.orderclient')),
            ],
            options={
                'db_table': 'OrderClientDetails',
                'unique_together': {('ocdorderclientid', 'ocdmenuid')},
            },
        ),
        migrations.AddField(
            model_name='orderclient',
            name='menus',
            field=models.ManyToManyField(through='RestaurantApp.Orderclientdetails', to='RestaurantApp.Menu'),
        ),
        migrations.AddField(
            model_name='orderclient',
            name='waiter_waiterid',
            field=models.ForeignKey(db_column='waiter_waiterid', on_delete=django.db.models.deletion.CASCADE, to='RestaurantApp.waiter'),
        ),
        migrations.AddField(
            model_name='menu',
            name='products',
            field=models.ManyToManyField(through='RestaurantApp.Productmenu', to='BodegaApp.Product'),
        ),
        migrations.AddField(
            model_name='client',
            name='rt_tableid',
            field=models.ForeignKey(db_column='rt_tableid', on_delete=django.db.models.deletion.CASCADE, to='RestaurantApp.restauranttable'),
        ),
    ]
