# Generated by Django 3.1.2 on 2020-10-08 14:14

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20201008_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='file',
            field=models.FileField(null=True, upload_to='Media/', validators=[app.models.validate_file, app.models.validate_file_size], verbose_name=''),
        ),
    ]
