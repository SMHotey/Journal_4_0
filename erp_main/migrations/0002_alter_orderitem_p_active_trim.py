# Generated by Django 5.1 on 2024-09-05 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp_main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='p_active_trim',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
