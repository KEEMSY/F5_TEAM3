
# Generated by Django 4.0.3 on 2022-03-30 13:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [

        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('commentapp', '0001_initial'),
        ('articleapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(

            name='CommentLikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.ForeignKey(db_column='comment', on_delete=django.db.models.deletion.CASCADE, to='commentapp.comment')),
                ('user', models.ForeignKey(db_column='user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'comment_likes',
            },
        ),
        migrations.CreateModel(
            name='ArticleLikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),

                ('article', models.ForeignKey(db_column='article', on_delete=django.db.models.deletion.CASCADE, to='articleapp.article')),
                ('user', models.ForeignKey(db_column='user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'article_likes',
            },
        ),
        migrations.AddConstraint(
            model_name='commentlikes',
            constraint=models.UniqueConstraint(fields=('user', 'comment'), name='unique_user_comment'),
        ),
        migrations.AddConstraint(
            model_name='articlelikes',
            constraint=models.UniqueConstraint(fields=('user', 'article'), name='unique_user_article'),
        ),
    ]
