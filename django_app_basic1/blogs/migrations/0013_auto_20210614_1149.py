# Generated by Django 2.1.7 on 2021-06-14 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0012_auto_20210614_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogtags',
            name='tag_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
