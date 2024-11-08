# Generated by Django 5.1.2 on 2024-11-05 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postsApp', '0005_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('portrait', 'Portrait'), ('nature', 'Nature'), ('architecture', 'Architecture'), ('animals', 'Animals'), ('plants', 'Plants'), ('objects', 'Objects')], default='other', max_length=20),
        ),
    ]
