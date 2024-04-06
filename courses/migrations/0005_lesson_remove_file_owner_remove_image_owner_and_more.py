# Generated by Django 4.2.11 on 2024-04-06 06:18

import courses.fields
import courses.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_alter_content_order_alter_module_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('order', courses.fields.OrderField(blank=True, null=True)),
                ('content', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to=courses.models.lesson_attachment_path)),
                ('file', models.FileField(blank=True, upload_to=courses.models.lesson_attachment_path)),
                ('video', models.URLField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.RemoveField(
            model_name='file',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='image',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='text',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='video',
            name='owner',
        ),
        migrations.AddField(
            model_name='module',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Content',
        ),
        migrations.DeleteModel(
            name='File',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.DeleteModel(
            name='Text',
        ),
        migrations.DeleteModel(
            name='Video',
        ),
        migrations.AddField(
            model_name='lesson',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='courses.module'),
        ),
    ]