# Generated by Django 2.0.2 on 2018-03-08 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_remove_profile_favourites'),
        ('catalog', '0002_auto_20180307_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='favourites',
            field=models.ManyToManyField(to='profiles.Profile'),
        ),
    ]
