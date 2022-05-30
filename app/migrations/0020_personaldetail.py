# Generated by Django 3.2.12 on 2022-04-28 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_delete_personaldetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personaldetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=1000)),
                ('phone', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'Personaldetail',
            },
        ),
    ]
