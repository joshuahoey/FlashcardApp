# Generated by Django 3.1.8 on 2021-07-01 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='cardTotal',
        ),
    ]
