# Generated by Django 3.1.7 on 2021-11-14 19:22

from django.db import migrations, models
import paneluser.models


class Migration(migrations.Migration):

    dependencies = [
        ('paneluser', '0002_auto_20211114_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to=paneluser.models.order_file_path),
        ),
    ]
