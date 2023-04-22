# Generated by Django 4.2 on 2023-04-22 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('time_when_posted', models.DateTimeField(auto_now_add=True)),
                ('post_content', models.TextField()),
                ('likes', models.IntegerField(default=0)),
                ('user_image', models.ImageField(blank=True, null=True, upload_to='user_images')),
            ],
        ),
    ]