# Generated by Django 3.2.10 on 2022-07-08 10:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownerurls',
            name='long_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.RemoveField(
            model_name='ownerurls',
            name='owner',
        ),
        migrations.AddField(
            model_name='ownerurls',
            name='owner',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ownerurls',
            name='short_url',
            field=models.URLField(blank=True, max_length=50, null=True),
        ),
    ]
