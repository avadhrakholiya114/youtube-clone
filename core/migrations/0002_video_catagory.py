# Generated by Django 5.0.1 on 2024-03-10 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='catagory',
            field=models.CharField(choices=[('public', 'public'), ('unlisted', 'unlisted'), ('Members only', 'Members only'), ('private', 'private')], default='other', max_length=100),
        ),
    ]
