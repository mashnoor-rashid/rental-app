# Generated by Django 2.0.2 on 2018-03-15 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_ad_add_fav'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='add_fav',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(blank=True, choices=[('Other', 'Other'), ('Home Renovation', 'Home Renovation'), ('Gardening', 'Gardening'), ('Power Tools', 'Power Tools'), ('Moving', 'Moving'), ('Garage', 'Garage'), ('Washroom', 'Washroom'), ('Kitchen', 'Kitchen'), ('Automobile', 'Automobile')], default='Other', help_text='Choose a cateogry (e.g. Moving, Gardening etc.)', max_length=20, unique=True),
        ),
    ]