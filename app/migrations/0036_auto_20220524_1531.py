# Generated by Django 3.2.12 on 2022-05-24 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0035_multipleimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='multipleimage',
            name='post',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.post'),
        ),
        migrations.DeleteModel(
            name='PostImage',
        ),
    ]
