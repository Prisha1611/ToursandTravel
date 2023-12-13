# Generated by Django 4.2.6 on 2023-12-11 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0006_testimonials'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('image_url', models.CharField(max_length=255)),
            ],
        ),
    ]
