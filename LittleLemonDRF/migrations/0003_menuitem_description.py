# Generated by Django 5.0.1 on 2024-01-13 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonDRF', '0002_menuitem_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='description',
            field=models.TextField(default='Item Description', max_length=400),
        ),
    ]