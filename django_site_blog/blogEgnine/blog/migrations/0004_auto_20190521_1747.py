# Generated by Django 2.2 on 2019-05-21 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190521_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='posts', to='blog.Category'),
        ),
    ]