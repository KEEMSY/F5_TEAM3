from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.CharField(default='', max_length=600)),
                ('name', models.CharField(default='', max_length=100)),
                ('tabom', models.CharField(default='', max_length=100)),
                ('desc', models.CharField(default='', max_length=600)),
                ('work', models.CharField(default='', max_length=600)),
                ('link', models.CharField(default='', max_length=600)),
                ('w_desc', models.CharField(default='', max_length=600)),
                ('info', models.CharField(default='', max_length=500)),
                ('date', models.CharField(default='', max_length=40)),
                ('recruit_site', models.CharField(max_length=40)),
                ('skills', models.CharField(default='Python', max_length=40)),
            ],
            options={
                'db_table': 'rocketpunch',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_pic', models.CharField(max_length=600)),
                ('news_title', models.CharField(max_length=100)),
                ('news_desc', models.TextField(null=True)),
                ('news_link', models.CharField(max_length=600)),
                ('news_date', models.CharField(blank=True, max_length=30)),
            ],
            options={
                'db_table': 'itnews',
            },
        ),
    ]
