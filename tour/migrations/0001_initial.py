# Generated by Django 4.2.7 on 2023-12-10 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=7000)),
                ('img1', models.ImageField(default='about.jpg', upload_to='aboutpage')),
                ('img2', models.ImageField(default='about.jpg', upload_to='aboutpage')),
                ('img3', models.ImageField(default='about.jpg', upload_to='aboutpage')),
                ('img4', models.ImageField(default='about.jpg', upload_to='aboutpage')),
                ('img5', models.ImageField(default='about.jpg', upload_to='aboutpage')),
            ],
        ),
    ]