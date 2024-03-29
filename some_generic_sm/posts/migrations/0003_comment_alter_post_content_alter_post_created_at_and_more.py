# Generated by Django 4.2.1 on 2023-07-02 10:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255, verbose_name='Content')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creation Datetime')),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.CharField(max_length=255, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Creation Datetime'),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Update Datetime'),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creation Datetime')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='posts.comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='posts.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='posts.post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='replying_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='posts.comment'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
