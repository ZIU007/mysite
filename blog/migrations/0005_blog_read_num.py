# Generated by Django 2.1.5 on 2021-07-01 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210630_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='read_num',
            field=models.IntegerField(default=0),
        ),
    ]
