# Generated by Django 4.0.3 on 2022-04-04 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0011_alter_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.FileField(blank=True, null=True, upload_to='uploads/%Y%m%d'),
        ),
    ]
