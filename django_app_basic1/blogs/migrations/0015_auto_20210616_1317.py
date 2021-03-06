# Generated by Django 2.1.7 on 2021-06-16 13:17

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0014_auto_20210616_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='blog_hashtags',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, 'Upskills'), (2, 'Recommend'), (3, 'Genneral'), (4, 'Food'), (5, 'New')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='blog_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blogs.BlogType'),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='create_by',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
