# Generated by Django 3.2.8 on 2021-10-31 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kpapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=250)),
                ('img1', models.ImageField(upload_to='inmakes_project')),
                ('desc1', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='place',
            name='img',
            field=models.ImageField(upload_to='inmakes_project'),
        ),
    ]
