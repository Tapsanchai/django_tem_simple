# Generated by Django 3.2.4 on 2021-06-18 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_js', '0003_auto_20210618_0728'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='js_blogtype',
            unique_together={('type_name',)},
        ),
    ]
