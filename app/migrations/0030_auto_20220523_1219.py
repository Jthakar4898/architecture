# Generated by Django 3.2.12 on 2022-05-23 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_alter_uploadproject_img1'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Portfoliopage',
        ),
        migrations.DeleteModel(
            name='Uploadproject',
        ),
    ]
