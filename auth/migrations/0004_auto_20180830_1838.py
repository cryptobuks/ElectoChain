# Generated by Django 2.1 on 2018-08-30 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20180830_1837'),
    ]

    operations = [
        migrations.RenameField(
            model_name='voter',
            old_name='adhaar_id',
            new_name='aadhaar_id',
        ),
    ]
