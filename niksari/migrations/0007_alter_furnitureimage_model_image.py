# Generated by Django 4.2.6 on 2023-11-06 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('niksari', '0006_rename_image_model_name_furnitureimage_image_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='furnitureimage',
            name='model_image',
            field=models.ImageField(upload_to='furnitureimage/'),
        ),
    ]
