# Generated by Django 4.2.4 on 2023-08-20 08:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_subscriber_received_fact_ids'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='confirmation_token',
            field=models.CharField(default=uuid.uuid4, max_length=36, unique=True),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]