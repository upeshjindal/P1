# Generated by Django 2.0 on 2017-12-06 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='id',
            field=models.PositiveSmallIntegerField(primary_key=True, serialize=False),
        ),
    ]