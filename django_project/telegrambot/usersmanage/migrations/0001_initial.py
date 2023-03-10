# Generated by Django 4.0.5 on 2022-06-23 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Назва відео')),
                ('video', models.CharField(max_length=300, verbose_name='FILE ID VIDEO')),
                ('description', models.TextField(max_length=100, null=True, verbose_name='Опис відео(про що відоео)')),
                ('category_code', models.CharField(max_length=30, verbose_name='Код категорії')),
                ('category_name', models.CharField(max_length=30, verbose_name='Назва категорії')),
            ],
            options={
                'verbose_name': 'Відео',
                'verbose_name_plural': 'Відео',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.BigIntegerField(default=1, unique=True, verbose_name='ID користувача Телеграм')),
                ('name', models.CharField(max_length=100, verbose_name="Ім'я користувача")),
                ('username', models.CharField(max_length=100, null=True, verbose_name='Username в Телеграмі')),
            ],
            options={
                'verbose_name': 'Користувач',
                'verbose_name_plural': 'Користувачі',
            },
        ),
    ]
