# Generated by Django 5.0 on 2023-12-08 15:48

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_alter_category_options_alter_photo_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
