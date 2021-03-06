# Generated by Django 3.0.1 on 2020-03-04 06:27

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200302_1319'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filepath', models.FileField(upload_to='uploads/', validators=[app.models.validate_file_size])),
            ],
        ),
    ]
