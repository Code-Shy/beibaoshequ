# Generated by Django 4.0.3 on 2022-05-22 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_article_delete_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='img/avatar/default_avatar.jpg', upload_to='img/avatar'),
        ),
    ]
