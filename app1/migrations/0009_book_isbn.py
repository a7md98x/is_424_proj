# Generated by Django 4.1 on 2023-12-02 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_genre_book_average_rating_book_edition_book_genres_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='ISBN',
            field=models.CharField(default=2, max_length=13, unique=True),
            preserve_default=False,
        ),
    ]
