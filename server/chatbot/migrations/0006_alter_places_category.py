# Generated by Django 5.0.4 on 2024-04-21 07:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0005_category_places_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='places',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='chatbot.category'),
        ),
    ]
