# Generated by Django 4.1.2 on 2022-11-17 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_article_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='publish',
            field=models.DateField(blank=True, null=True),
        ),
    ]
