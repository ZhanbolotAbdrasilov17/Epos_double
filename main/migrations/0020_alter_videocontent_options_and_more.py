# Generated by Django 4.1 on 2022-09-11 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_videocontent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='videocontent',
            options={'ordering': ['name'], 'verbose_name': 'Видео_Контент'},
        ),
        migrations.RenameField(
            model_name='videocontent',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='videocontent',
            name='file',
        ),
        migrations.AddField(
            model_name='videocontent',
            name='link',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Ссылка'),
        ),
    ]
