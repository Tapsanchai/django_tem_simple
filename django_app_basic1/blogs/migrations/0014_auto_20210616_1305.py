# Generated by Django 2.1.7 on 2021-06-16 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0013_auto_20210614_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]