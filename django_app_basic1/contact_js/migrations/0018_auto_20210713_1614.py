# Generated by Django 2.2 on 2021-07-13 09:14

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('contact_js', '0017_auto_20210713_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alternatephonemodel',
            name='test_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
    ]
