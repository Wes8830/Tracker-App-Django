# Generated by Django 3.2.5 on 2022-01-12 23:53

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0006_alter_client_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='desc',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='please enter a description', max_length=512),
        ),
    ]