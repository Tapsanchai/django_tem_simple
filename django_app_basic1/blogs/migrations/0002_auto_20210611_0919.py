# Generated by Django 2.1.7 on 2021-06-11 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='create_by',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
