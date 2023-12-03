# Generated by Django 4.1 on 2023-12-02 21:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_alter_book_genres'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='genres',
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='average_rating',
            field=models.FloatField(default=0.0, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
    ]