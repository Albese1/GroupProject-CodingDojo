# Generated by Django 2.2 on 2020-08-03 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0002_auto_20200802_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(default='0', max_length=1),
        ),
    ]