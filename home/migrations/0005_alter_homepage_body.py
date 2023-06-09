# Generated by Django 4.1.3 on 2022-11-25 15:04

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_homepage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField([('title', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(help_text='text to display', required=True))])), ('cards', wagtail.blocks.StructBlock([('cards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.TextBlock(help_text='optional text for this card. max len 255 char', max_length=255, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='image will be automagically cropped 570px by 370px'))])))]))], blank=True, null=True, use_json_field=None),
        ),
    ]
