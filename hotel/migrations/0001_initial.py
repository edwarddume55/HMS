# Generated by Django 5.1.3 on 2024-11-07 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('catgory', models.CharField(choices=[('YAC', 'AC'), ('DEL', 'DELUXE'), ('KIN', 'KING'), ('QUE', 'QUEEN')], max_length=3)),
                ('beds', models.IntegerField()),
            ],
        ),
    ]
