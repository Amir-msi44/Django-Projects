# Generated by Django 5.0.6 on 2024-05-16 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_user_is_author_alter_user_special_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Email'),
        ),
    ]