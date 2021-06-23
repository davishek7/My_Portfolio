# Generated by Django 3.2.4 on 2021-06-23 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avishek', '0002_auto_20210226_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='github_repo',
            field=models.URLField(blank=True, default='https://github.com/davishek7/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='details',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
