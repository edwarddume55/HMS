# Generated by Django 5.1.3 on 2024-11-08 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_booking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='catgory',
            new_name='category',
        ),
    ]
