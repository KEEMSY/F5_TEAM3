# Generated by Django 4.0.3 on 2022-04-07 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0008_alter_article_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]