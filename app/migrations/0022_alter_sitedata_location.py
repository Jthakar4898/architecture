# Generated by Django 3.2.12 on 2022-05-10 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_sitedata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitedata',
            name='location',
            field=models.CharField(max_length=50),
        ),
    ]
