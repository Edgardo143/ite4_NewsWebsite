# Generated by Django 5.0 on 2023-12-16 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('politics', 'Politics'), ('entertainment', 'Entertainment'), ('sports', 'Sports')], max_length=20)),
            ],
        ),
    ]
