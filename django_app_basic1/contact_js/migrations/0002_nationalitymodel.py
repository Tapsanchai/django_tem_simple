# Generated by Django 2.1.7 on 2021-07-01 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_js', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NationalityModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nationality_title', models.CharField(blank=True, max_length=120, unique=True)),
            ],
        ),
    ]
