# Generated by Django 4.0.5 on 2022-06-27 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersmanage', '0006_item_is_published_alter_item_subcategory_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Опубліковано (так | ні)'),
        ),
    ]
