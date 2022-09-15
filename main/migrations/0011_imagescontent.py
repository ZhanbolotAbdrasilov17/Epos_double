# Generated by Django 4.1 on 2022-09-08 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_authors_articlesarchive_text_en_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagesContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Картинка')),
                ('title_ru', models.CharField(blank=True, max_length=100, null=True, verbose_name='Картинка')),
                ('title_ky', models.CharField(blank=True, max_length=100, null=True, verbose_name='Картинка')),
                ('title_en', models.CharField(blank=True, max_length=100, null=True, verbose_name='Картинка')),
                ('file', models.ImageField(blank=True, null=True, upload_to='work_images')),
            ],
            options={
                'verbose_name': 'Галерея_Контент',
            },
        ),
    ]
