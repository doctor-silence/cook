from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey

class Category(MPTTModel):
    name = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=100)
    parent = TreeForeignKey('self', related_name='children', on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):   #Отображаем родителя в админке
        return self.name
    class MPTTMeta:
        order_insertion_by = ['name']

class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=100)


    def __str__(self):   #Отображаем родителя в админке
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    image = models.ImageField(upload_to='articles/', verbose_name='Картинка')
    text = models.TextField(verbose_name='Текст')
    category = models.ForeignKey(Category, related_name='post', on_delete=models.SET_NULL, null=True, verbose_name='Категория')
    tags = models.ManyToManyField(Tag, related_name='post', verbose_name='Тег')
    create_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, default='')

    def __str__(self):   #Отображаем родителя в админке
        return self.title[0:16]

    def get_absolute_url(self):
        return reverse("post_single", kwargs={"slug": self.category.slug, "post_slug": self.slug})


class Recipe(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    serves = models.CharField(max_length=50, verbose_name='Подача')
    prep_time = models.PositiveIntegerField(default=0, verbose_name='Время подготовки')
    cook_time = models.PositiveIntegerField(default=0, verbose_name='Время приготовления')
    ingredients = models.TextField(verbose_name='Ингредиенты')
    directions = models.TextField(verbose_name='Описание')
    post = models.ForeignKey(Post, related_name='recipe', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Пост')



class Comment(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    email = models.CharField(max_length=100)
    website = models.CharField(max_length=150)
    message = models.TextField(max_length=500)
    post = models.ForeignKey(Post, related_name='comment', on_delete=models.CASCADE)






