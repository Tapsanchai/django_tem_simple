# Generated by Django 2.1.7 on 2021-07-01 04:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact_js', '0012_alternateemailmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alternateemailmodel',
            old_name='phone_type',
            new_name='email_type',
        ),
    ]