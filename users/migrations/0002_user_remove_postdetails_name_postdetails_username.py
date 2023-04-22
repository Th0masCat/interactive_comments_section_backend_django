# Generated by Django 4.2 on 2023-04-22 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=32, primary_key=True, serialize=False, unique=True)),
                ('email', models.EmailField(max_length=32, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='postdetail',
            name='name',
        ),
        migrations.AddField(
            model_name='postdetail',
            name='username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
    ]
