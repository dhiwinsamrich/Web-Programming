# Generated by Django 4.0.6 on 2022-07-17 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(default='images/default.jpg', upload_to='images'),
        ),
    ]
