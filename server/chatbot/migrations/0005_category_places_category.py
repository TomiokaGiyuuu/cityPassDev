# Generated by Django 5.0.4 on 2024-04-21 06:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0004_remove_places_schedule_remove_schedule_day_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(choices=[('Музей', 'Музей'), ('Театр', 'Театр'), ('Монумент', 'Монумент'), ('Развлечения', 'Развлечения'), ('Мечеть', 'Мечеть'), ('Парк', 'Парк'), ('Искусство', 'Искусство'), ('Культурный Центр', 'Культурный Центр'), ('Без категории', 'Без категории')], max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='places',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='chatbot.category'),
        ),
    ]
