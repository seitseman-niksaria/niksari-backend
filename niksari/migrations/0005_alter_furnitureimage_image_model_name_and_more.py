# Generated by Django 4.2.5 on 2023-11-06 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('niksari', '0004_alter_instruction_instruction_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='furnitureimage',
            name='image_model_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='instruction',
            name='instruction_name',
            field=models.CharField(default='instruction', max_length=50),
        ),
    ]
