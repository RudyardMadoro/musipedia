# Generated by Django 3.2.5 on 2021-07-27 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0002_auto_20210726_2033'),
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='songs',
            field=models.ManyToManyField(blank=True, to='songs.Song'),
        ),
    ]