# Generated by Django 3.2.5 on 2021-07-26 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0003_alter_artist_picture'),
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='artist',
        ),
        migrations.AddField(
            model_name='song',
            name='artits',
            field=models.ManyToManyField(blank=True, to='apis.Artist'),
        ),
    ]
