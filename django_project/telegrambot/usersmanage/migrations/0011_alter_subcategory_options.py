# Generated by Django 4.0.5 on 2022-07-13 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usersmanage', '0010_subcategory_alter_item_subcategory_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subcategory',
            options={'ordering': ['title'], 'verbose_name': 'Підкатегорія', 'verbose_name_plural': 'Підкатегорії'},
        ),
    ]
