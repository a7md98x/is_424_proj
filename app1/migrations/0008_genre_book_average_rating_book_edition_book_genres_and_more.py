# Generated by Django 4.1 on 2023-12-02 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_book_author_book_language_book_pages_customers_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='average_rating',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='book',
            name='edition',
            field=models.PositiveIntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='genres',
            field=models.ManyToManyField(blank=True, related_name='type', to='app1.book'),
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]
