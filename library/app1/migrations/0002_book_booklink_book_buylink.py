# Generated by Django 4.2.4 on 2023-10-10 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='booklink',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='buylink',
            field=models.URLField(null=True),
        ),
    ]
