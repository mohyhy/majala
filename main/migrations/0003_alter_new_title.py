# Generated by Django 4.0.6 on 2022-12-25 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_blog_main_blog_main2_new_main_new_main2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]