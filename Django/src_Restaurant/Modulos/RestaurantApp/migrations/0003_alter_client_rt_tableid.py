# Generated by Django 3.2.7 on 2021-12-06 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RestaurantApp', '0002_menu_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='rt_tableid',
            field=models.ForeignKey(db_column='rt_tableid', on_delete=django.db.models.deletion.CASCADE, related_name='rt_tableid_related', to='RestaurantApp.restauranttable'),
        ),
    ]
