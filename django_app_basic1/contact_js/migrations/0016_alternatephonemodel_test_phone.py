# Generated by Django 2.2 on 2021-07-13 08:23

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('contact_js', '0015_auto_20210704_2228'),
    ]

    operations = [
        migrations.AddField(
            model_name='alternatephonemodel',
            name='test_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
    ]
