# Generated by Django 4.1.4 on 2023-05-11 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_property_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='price_in_text',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
