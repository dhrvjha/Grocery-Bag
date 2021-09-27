# Generated by Django 3.2.4 on 2021-09-27 16:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bag', '0003_auto_20210926_1415'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, help_text='uuid used for urls', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('quantity', models.CharField(max_length=100)),
                ('date', models.DateField(null=True)),
                ('status', models.CharField(choices=[('PD', 'PENDING'), ('NT', 'NOT AVAILABLE'), ('BT', 'BOUGHT')], max_length=25)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='item',
        ),
    ]
