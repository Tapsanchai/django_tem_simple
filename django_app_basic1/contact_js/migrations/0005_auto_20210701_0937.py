# Generated by Django 2.1.7 on 2021-07-01 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_js', '0004_auto_20210701_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmodel',
            name='home',
            field=models.CharField(blank=True, max_length=120, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='contactmodel',
            name='main_fax',
            field=models.CharField(blank=True, max_length=120, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='contactmodel',
            name='work',
            field=models.CharField(blank=True, max_length=120, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='contactmodel',
            name='work_phone_exten',
            field=models.CharField(blank=True, max_length=120, null=True, unique=True),
        ),
    ]
