# Generated by Django 2.1.3 on 2018-11-29 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('routine', '0004_auto_20181130_0237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='routine.Department'),
        ),
    ]
