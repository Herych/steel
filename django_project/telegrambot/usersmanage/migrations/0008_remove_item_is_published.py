# Generated by Django 4.0.5 on 2022-06-29 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usersmanage', '0007_alter_item_is_published'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='is_published',
        ),
    ]