# Generated by Django 3.0.6 on 2020-07-30 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0002_remove_events_posted_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='video_url',
            field=models.TextField(default='https://www.youtube.com/embed/foyufD52aog'),
            preserve_default=False,
        ),
    ]