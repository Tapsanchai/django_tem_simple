# Generated by Django 2.1.7 on 2021-07-01 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_js', '0003_contactmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmodel',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
