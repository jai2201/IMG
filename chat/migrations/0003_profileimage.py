# Generated by Django 3.1.6 on 2021-02-17 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20210215_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='myimage')),
            ],
        ),
    ]
