# Generated by Django 2.2 on 2021-07-22 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_js', '0023_testcheckboxmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='testcheckboxmodel',
            name='chk_dender2',
            field=models.IntegerField(blank=True, choices=[(1, 'Female/ผู้หญิง'), (2, 'Male/ผู้ชาย'), (3, 'Other/อื่นๆ'), (4, 'None/ไม่ระบุเพศ')], null=True),
        ),
    ]
