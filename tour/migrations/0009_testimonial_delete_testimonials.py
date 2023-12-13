# Generated by Django 4.2.6 on 2023-12-11 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0008_galleryimage_delete_teammember'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='testimonials/')),
                ('quote', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Testimonials',
        ),
    ]