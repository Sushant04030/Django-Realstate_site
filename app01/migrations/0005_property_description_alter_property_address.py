# Generated by Django 4.1.4 on 2023-05-10 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_alter_city_options_alter_gallery_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='address',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]