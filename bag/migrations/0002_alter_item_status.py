# Generated by Django 3.2.4 on 2021-09-26 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bag', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='status',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]