# Generated by Django 4.1.3 on 2023-01-02 14:20

from django.db import migrations
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=froala_editor.fields.FroalaField(),
        ),
    ]
