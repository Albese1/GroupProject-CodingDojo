# Generated by Django 2.2 on 2020-08-01 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0003_movie_video_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cinoroom',
            name='room',
            field=models.CharField(default='A1', max_length=2),
        ),
    ]