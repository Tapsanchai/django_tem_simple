# Generated by Django 2.1.7 on 2021-06-18 01:46

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog_js', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JS_Blogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('content', models.TextField()),
                ('create_by', models.CharField(max_length=255, null=True)),
                ('blog_hashtags', multiselectfield.db.fields.MultiSelectField(choices=[(1, 'Computer'), (2, 'Math'), (3, 'Eng'), (4, 'Technology')], max_length=255, null=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('time_updated', models.DateTimeField(auto_now=True)),
                ('blog_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog_js.JS_BlogType')),
            ],
        ),
    ]
