# Generated by Django 4.1.4 on 2022-12-17 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salons', '0009_alter_appointment_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='telegram_id',
            field=models.BigIntegerField(),
        ),
    ]
