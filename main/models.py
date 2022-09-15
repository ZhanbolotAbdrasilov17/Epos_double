from django.db import models
from ckeditor.fields import RichTextField



class Logo(models.Model):
    logo = models.ImageField(upload_to='logo', blank=True, null=True, verbose_name='Логотип')

    def __str__(self):
        return 'Логотип'

    class Meta:
        verbose_name_plural = 'Логотип'
        verbose_name = 'Логотип'

class Statistic(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название статистики', blank=True, null=True)
    statistic = models.CharField(max_length=100, verbose_name='Статистика', blank=True, null=True)
    lower = models.CharField(max_length=100, verbose_name='Нижняя цифра', blank=True, null=True)
    comments = models.CharField(max_length=100, verbose_name='Комментарий', blank=True, null=True)

    def __str__(self):
        return f'{self.id}.  {self.title}'

    class Meta:
        verbose_name_plural = 'Главная - Статистика'
        verbose_name = 'Главная - Статистика'


class Categories(models.Model):
    category_name = models.CharField(max_length=200, verbose_name='Название категории')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'категория'


class CategoriesForArchieved(models.Model):
    category_name = models.CharField(max_length=200, verbose_name='Название категории')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = 'Категории для архивных статей'
        verbose_name = 'Категория для архивной статьи'


class ArticlesArchive(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название статьи')
    category_name = models.ForeignKey(CategoriesForArchieved, on_delete=models.CASCADE, related_name="Категории")
    date = models.CharField(max_length=200, blank=True, null=True, verbose_name='Дата создания статьи')
    text = models.TextField(verbose_name="Текст")
    image = models.ImageField(upload_to='project-images', verbose_name='Изображение')
    pdf = models.FileField()
    word = models.FileField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Архивные Статьи'
        verbose_name = 'Архивная Статья'


class Articles(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название статьи')
    category_name = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name="Категории")
    date = models.CharField(max_length=200, blank=True, null=True, verbose_name='Дата создания статьи')
    text = models.TextField(verbose_name="Текст")
    image = models.ImageField(upload_to='project-images', verbose_name='Изображение')
    pdf = models.FileField()
    word = models.FileField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Статьи'
        verbose_name = 'Статья'


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название новости')
    date = models.CharField(max_length=200, blank=True, null=True, verbose_name='Дата создания новости')
    text = models.TextField(verbose_name="Текст")
    image = models.ImageField(upload_to='project-images', verbose_name='Изображение на показ')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Новости'
        verbose_name = 'Новость'


class PartnerCategory(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название категории',)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Категории партнёров'
        verbose_name = 'Кетегория партнёра'


class Partner(models.Model):
    category = models.ForeignKey(PartnerCategory, on_delete=models.CASCADE, verbose_name='Категория партнера',
                                 related_name='category_partners')
    title = models.CharField(max_length=200, verbose_name='Название партнёра')
    image = models.ImageField(upload_to='partner-image', blank=True, null=True, verbose_name='Логотип партнера')
    link = models.CharField(max_length=200, blank=True, null=True, verbose_name='Ссылка на сайт партнера')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Партнёры'
        verbose_name = 'Партнёр'


class Gallery(models.Model):
    title = models.CharField(max_length=200, verbose_name='Имя автора')
    date = models.CharField(max_length=200, blank=True, null=True, verbose_name='Дата жизни')
    image = models.ImageField(upload_to='gallery-images', verbose_name='Фото автора')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Галерея'
        verbose_name = 'Галерея'


class SocialMedia(models.Model):
    instagram = models.CharField(max_length=200, verbose_name='Инстаграм')
    whatsapp = models.CharField(max_length=200, verbose_name='Ватсап')
    facebook = models.CharField(max_length=200, verbose_name='Фейсбук')

    def __str__(self):
        return 'Социальные сети'

    class Meta:
        verbose_name_plural = 'Социальные сети'
        verbose_name = 'Социальная сеть'


class Partners(models.Model):
    partner_name = models.CharField(max_length=200, verbose_name="Название партнера")
    image = models.ImageField(upload_to='partners_images', verbose_name='Фото', blank=True, null=True)

    def __str__(self):
        return self.partner_name

    class Meta:
        verbose_name = 'Партнёры'


class AuthorCategory(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Авторам - Категория'
        verbose_name_plural = 'Авторам - Категория'


class Authors(models.Model):
    category = models.ForeignKey(AuthorCategory, on_delete=models.DO_NOTHING, verbose_name='Категория',
                                 related_name='author_category')
    title = models.CharField(max_length=200, verbose_name='Оглавление')
    text = models.TextField(verbose_name="Текст")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Авторам'
        verbose_name_plural = 'Авторам'


class ImagesContent(models.Model):
    title = models.CharField(max_length=100, verbose_name="Картинка", blank=True, null=True)
    file = models.ImageField(null=True, blank=True, upload_to="work_images")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Галерея Контент'


class MainTagline(models.Model):
    title = models.CharField(max_length=200, verbose_name='Главный слоган', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Галерея Слоган'
        verbose_name = 'Галерея Слоган'


class FirstTagline(models.Model):
    title = models.CharField(max_length=200, verbose_name='Первый слоган', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Первый слоган'
        verbose_name = 'Первый слоган'


class Employees(models.Model):
    name = models.CharField(max_length=200, verbose_name='ФИО')
    text = models.TextField(verbose_name="Текст")
    image = models.ImageField(upload_to='project-images', verbose_name='Изображение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Сотрудники'
        verbose_name = 'Сотрудник'


class Content(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название картинки", blank=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to="content")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Картинки'
        verbose_name = 'Картинки'
        ordering = ['name']


class LizerCategory(models.Model):
    title = models.CharField(max_length=100, verbose_name='Эквалайзер Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Эквалайзер - Категория'
        verbose_name = 'Эквалайзер - Категория'


class Lizer(models.Model):
    category = models.ForeignKey(LizerCategory, on_delete=models.CASCADE, verbose_name='Категория')
    title = models.CharField(max_length=100, verbose_name='Эквалайзер')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Эквалайзер'
        verbose_name = 'Эквалайзер'
