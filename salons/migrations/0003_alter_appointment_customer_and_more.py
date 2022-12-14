# Generated by Django 4.1.4 on 2022-12-08 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('salons', '0002_alter_providerschedule_provider_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='salons.customer', verbose_name='клиент'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='salons.provider', verbose_name='мастер'),
        ),
    ]
