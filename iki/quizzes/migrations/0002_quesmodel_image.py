# Generated by Django 4.1.3 on 2022-11-18 15:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quesmodel',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='question/', verbose_name='image'),
            preserve_default=False,
        ),
    ]
