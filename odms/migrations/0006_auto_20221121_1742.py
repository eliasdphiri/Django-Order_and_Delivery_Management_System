# Generated by Django 2.1.15 on 2022-11-21 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('odms', '0005_auto_20221121_1730'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': 'Customer Orders'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Products'},
        ),
    ]
