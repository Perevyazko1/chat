# Generated by Django 4.1.7 on 2023-02-21 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SimpleUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default=None, upload_to='images/')),
            ],
        ),
        migrations.DeleteModel(
            name='RoomConnection',
        ),
    ]
