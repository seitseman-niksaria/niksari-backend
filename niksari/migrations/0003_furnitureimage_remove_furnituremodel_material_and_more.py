# Generated by Django 4.2.5 on 2023-11-06 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('niksari', '0002_alter_furnituremodel_upholstery'),
    ]

    operations = [
        migrations.CreateModel(
            name='FurnitureImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_image', models.ImageField(upload_to='')),
                ('image_model_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='furnituremodel',
            name='material',
        ),
        migrations.RemoveField(
            model_name='furnituremodel',
            name='surface_finish',
        ),
        migrations.RemoveField(
            model_name='furnituremodel',
            name='upholstery',
        ),
        migrations.RemoveField(
            model_name='instruction',
            name='material',
        ),
        migrations.RemoveField(
            model_name='instruction',
            name='surface_finish',
        ),
        migrations.RemoveField(
            model_name='instruction',
            name='upholstery',
        ),
        migrations.AddField(
            model_name='furnituremodel',
            name='instructions',
            field=models.ManyToManyField(to='niksari.instruction'),
        ),
        migrations.AddField(
            model_name='furnituremodel',
            name='leather',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='furnituremodel',
            name='outdoor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='instruction',
            name='instruction_name',
            field=models.CharField(default='lether 1', max_length=30),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='furnituremodel',
            name='furniture_name',
            field=models.CharField(max_length=30),
        ),
        migrations.DeleteModel(
            name='Material',
        ),
        migrations.DeleteModel(
            name='SurfaceFinish',
        ),
        migrations.DeleteModel(
            name='Upholstery',
        ),
        migrations.AddField(
            model_name='furnitureimage',
            name='furniture_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='niksari.furnituremodel'),
        ),
    ]
