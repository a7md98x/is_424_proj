# Generated by Django 4.1 on 2023-11-28 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_customers_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customers',
            name='password',
        ),
        migrations.RemoveField(
            model_name='customers',
            name='username',
        ),
    ]