# Generated by Django 2.1 on 2018-09-03 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BTESDB', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='db_part',
            name='Approved',
        ),
        migrations.RemoveField(
            model_name='db_part',
            name='DataQuality',
        ),
        migrations.RemoveField(
            model_name='db_part',
            name='DataRelevance',
        ),
        migrations.RemoveField(
            model_name='db_part',
            name='Documentation',
        ),
        migrations.RemoveField(
            model_name='db_part',
            name='Incomplete',
        ),
        migrations.RemoveField(
            model_name='db_part',
            name='Rationality',
        ),
        migrations.RemoveField(
            model_name='db_part',
            name='UseEDPValueOfFloorAbove',
        ),
        migrations.RemoveField(
            model_name='db_part',
            name='correlation',
        ),
        migrations.RemoveField(
            model_name='db_part',
            name='default_units',
        ),
        migrations.RemoveField(
            model_name='db_part',
            name='dimension',
        ),
        migrations.RemoveField(
            model_name='db_part',
            name='directional',
        ),
    ]
