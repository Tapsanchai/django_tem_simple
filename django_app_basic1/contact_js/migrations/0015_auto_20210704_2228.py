# Generated by Django 2.1.7 on 2021-07-04 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_js', '0014_personaladdressmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alternateemailmodel',
            name='alternate_email',
            field=models.EmailField(blank=True, max_length=120, unique=True),
        ),
    ]