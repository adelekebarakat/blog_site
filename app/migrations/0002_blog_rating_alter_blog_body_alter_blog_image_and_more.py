# Generated by Django 4.2.4 on 2023-09-08 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='rating',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=models.TextField(help_text='compulsory'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(help_text='compulsory', upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(help_text='compulsory', max_length=100),
        ),
    ]
