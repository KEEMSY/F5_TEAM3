# Generated by Django 4.0.3 on 2022-03-30 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0009_alter_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.URLField(blank=True, max_length=250),
        ),
    ]
