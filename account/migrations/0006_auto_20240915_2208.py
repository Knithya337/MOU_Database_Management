# Generated by Django 3.1 on 2024-09-15 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20240915_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createmou',
            name='pdf_doc',
            field=models.FileField(upload_to='documents/'),
        ),
    ]
