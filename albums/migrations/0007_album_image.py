# Generated by Django 4.0.4 on 2022-05-11 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0006_remove_album_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
