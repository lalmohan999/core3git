# Generated by Django 4.1.3 on 2023-01-06 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_content'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Catergory',
            new_name='Category',
        ),
    ]