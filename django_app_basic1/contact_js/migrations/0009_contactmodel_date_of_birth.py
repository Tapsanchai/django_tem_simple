# Generated by Django 2.1.7 on 2021-07-01 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_js', '0008_alternatephonemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmodel',
            name='date_of_birth',
            field=models.DateField(blank=True, max_length=120, null=True),
        ),
    ]
