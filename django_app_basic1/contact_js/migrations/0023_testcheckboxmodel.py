# Generated by Django 2.2 on 2021-07-22 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_js', '0022_auto_20210715_1118'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestCheckboxModel',
            fields=[
                ('chk_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('chk_name', models.CharField(blank=True, max_length=255)),
                ('chk_gender', models.ManyToManyField(blank=True, to='contact_js.GendersModel')),
            ],
        ),
    ]
