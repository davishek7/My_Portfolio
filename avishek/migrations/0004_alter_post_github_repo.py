# Generated by Django 3.2.4 on 2021-06-23 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avishek', '0003_auto_20210623_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='github_repo',
            field=models.URLField(blank=True, null=True),
        ),
    ]
