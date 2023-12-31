# Generated by Django 4.2.7 on 2023-11-29 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yummier1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_visible', models.BooleanField(verbose_name=True)),
                ('image', models.ImageField(upload_to='photos/')),
            ],
        ),
    ]
