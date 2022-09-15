from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(Statistic)
class StatisticTranslation(TranslationOptions):
    fields = ('title', 'comments',)

@register(Articles)
class ArticlesTranslation(TranslationOptions):
    fields = ('title', 'text',)

@register(ArticlesArchive)
class ArticlesTranslation(TranslationOptions):
    fields = ('title', 'text',)

@register(News)
class NewsTranslation(TranslationOptions):
    fields = ('title', 'text',)

@register(Authors)
class AuthorsTranslation(TranslationOptions):
    fields = ('title', 'text',)

@register(ImagesContent)
class ImageContentTranslation(TranslationOptions):
    fields = ('title',)

@register(PartnerCategory)
class PartnerCategoryTranslation(TranslationOptions):
    fields = ('title',)

@register(Partner)
class PartnerTranslation(TranslationOptions):
    fields = ('title',)

@register(MainTagline)
class MainTaglineTranslation(TranslationOptions):
    fields = ('title',)

@register(Employees)
class EmployeesTranslation(TranslationOptions):
    fields = ('name', 'text')

