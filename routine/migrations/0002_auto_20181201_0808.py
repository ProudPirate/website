# Generated by Django 2.1.3 on 2018-12-01 02:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('routine', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='routine',
            unique_together={('day', 'period', 'section')},
        ),
    ]
