# Generated by Django 2.2 on 2021-07-13 15:52

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('contact_js', '0018_auto_20210713_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alternatephonemodel',
            name='test_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='TH'),
        ),
    ]
