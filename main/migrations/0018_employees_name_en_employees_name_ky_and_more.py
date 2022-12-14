# Generated by Django 4.1 on 2022-09-11 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_employees'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='name_en',
            field=models.CharField(max_length=200, null=True, verbose_name='ФИО'),
        ),
        migrations.AddField(
            model_name='employees',
            name='name_ky',
            field=models.CharField(max_length=200, null=True, verbose_name='ФИО'),
        ),
        migrations.AddField(
            model_name='employees',
            name='name_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='ФИО'),
        ),
        migrations.AddField(
            model_name='employees',
            name='text_en',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='employees',
            name='text_ky',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='employees',
            name='text_ru',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
    ]
