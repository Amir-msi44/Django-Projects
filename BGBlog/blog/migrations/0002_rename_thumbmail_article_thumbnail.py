# Generated by Django 4.1 on 2024-04-28 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='thumbmail',
            new_name='thumbnail',
        ),
    ]
