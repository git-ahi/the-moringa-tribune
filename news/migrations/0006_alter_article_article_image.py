# Generated by Django 4.0a1 on 2021-10-05 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_article_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default='trendy-block-quote-modern-template_1035-18965.jpg', upload_to='articles/'),
        ),
    ]
