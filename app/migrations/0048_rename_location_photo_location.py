# Generated by Django 3.2.12 on 2022-05-25 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0047_category_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='Location',
            new_name='location',
        ),
    ]
