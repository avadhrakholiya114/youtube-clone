# Generated by Django 5.0.1 on 2024-03-10 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_video_catagory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='catagory',
            field=models.CharField(choices=[('game', 'Gaming'), ('music', 'Music'), ('beauty', 'Beauty'), ('education', 'Education'), ('comedy', 'Comedy'), ('food', 'Food'), ('technology', 'Technology'), ('travel', 'Travel'), ('sports', 'Sports'), ('lifestyle', 'Lifestyle'), ('news', 'News'), ('entertainment', 'Entertainment'), ('other', 'Other')], default='other', max_length=100),
        ),
    ]
