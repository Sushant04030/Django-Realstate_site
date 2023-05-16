# Generated by Django 4.1.4 on 2023-05-09 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_gallery_property'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'City', 'verbose_name_plural': 'Cities'},
        ),
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name': 'Gallery', 'verbose_name_plural': 'Galleries'},
        ),
        migrations.AlterModelOptions(
            name='property',
            options={'verbose_name': 'Property', 'verbose_name_plural': 'Properties'},
        ),
        migrations.AlterField(
            model_name='gallery',
            name='title',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='area',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
    ]
