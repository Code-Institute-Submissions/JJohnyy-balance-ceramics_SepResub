# Generated by Django 3.2 on 2022-08-18 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mugs',
            options={'verbose_name_plural': 'Mugs'},
        ),
        migrations.AlterModelOptions(
            name='mugscategory',
            options={'verbose_name_plural': 'MugCategories'},
        ),
    ]
