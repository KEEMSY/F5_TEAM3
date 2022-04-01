# Generated by Django 4.0.3 on 2022-03-30 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0004_alter_profile_skill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='skill',
            field=models.CharField(blank=True, choices=[('Android', 'Android'), ('IOS', 'IOS'), ('C++', 'C++'), ('C#', 'C#'), ('Java', 'Java'), ('PHP', 'PHP'), ('Python', 'Python'), ('Ruby', 'Ruby'), ('JSP', 'JSP'), ('Node.js', 'Node.js'), ('AngularJS', 'AngularJS'), ('jQuery', 'jQuery'), ('ASP.NET', 'ASP.NET'), (None, '없음')], max_length=100),
        ),
    ]