# Generated by Django 3.0.1 on 2020-03-04 06:34

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='filepath',
            field=models.ImageField(upload_to='uploads/', validators=[app.models.validate_file_size]),
        ),
    ]