# Generated by Django 2.1.7 on 2021-07-01 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contact_js', '0013_auto_20210701_1106'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalAddressModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_1', models.CharField(blank=True, max_length=255)),
                ('address_2', models.CharField(blank=True, max_length=255, null=True)),
                ('building', models.CharField(blank=True, max_length=255, null=True)),
                ('district', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255)),
                ('province', models.CharField(blank=True, max_length=255, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=255, null=True)),
                ('primary_status', models.BooleanField(default=False)),
                ('alignment_status', models.BooleanField(default=False)),
                ('contact_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='contact_js.ContactModel')),
            ],
        ),
    ]
