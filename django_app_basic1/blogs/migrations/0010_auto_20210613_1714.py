# Generated by Django 2.1.7 on 2021-06-13 17:14

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0009_auto_20210613_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='blog_hashtags',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, 'Upskills'), (2, 'Recommend'), (3, 'Genneral'), (4, 'Food')], max_length=255, null=True),
        ),
    ]
