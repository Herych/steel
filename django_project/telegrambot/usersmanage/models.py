from django.db import models


# Create your models here.
class TimeBaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class User(TimeBaseModel):
    class Meta:
        verbose_name = 'Користувач'
        verbose_name_plural = 'Користувачі'

    id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField(unique=True, default=1, verbose_name='ID користувача Телеграм')
    name = models.CharField(max_length=100, verbose_name="Ім'я користувача")
    username = models.CharField(max_length=100, verbose_name='Username в Телеграмі', null=True)

    def __str__(self):
        return f"№{self.id} ({self.user_id} - {self.name})"


class Item(TimeBaseModel):
    class Meta:
        verbose_name = 'Відео'
        verbose_name_plural = 'Відео'

    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Назва відео', max_length=50)
    video = models.CharField(verbose_name='FILE ID VIDEO', max_length=300)
    description = models.TextField(verbose_name='Опис відео(про що відоео)', max_length=1000, null=True)
#    is_published = models.BooleanField(default=True, verbose_name='Опубліковано (так | ні)')

    category_code = models.CharField(default=1, verbose_name='Код категорії', max_length=30,)
    # category_name = models.CharField(verbose_name='Назва категорії', max_length=30)
    category_name = models.ForeignKey('Category', on_delete=models.PROTECT, null=True,  verbose_name='Назва категорії')
    subcategory_code = models.CharField(default=1, verbose_name="Код підкатегорії", max_length=20)
    # subcategory_name = models.CharField(verbose_name="Назва підкатегорії", max_length=30)
    subcategory_name = models.ForeignKey('SubCategory', on_delete=models.PROTECT, null=True, verbose_name="Назва підкатегорії")

    def __str__(self):
        return f"{self.name}"


class Category(TimeBaseModel):
    title = models.CharField(max_length=30, verbose_name='Назва категорії', db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категоря'
        verbose_name_plural = 'Категорії'
        ordering = ['title']


class SubCategory(TimeBaseModel):
    title = models.CharField(max_length=30, verbose_name='Назва підкатегорії', db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Підкатегорія'
        verbose_name_plural = 'Підкатегорії'
        ordering = ['title']

