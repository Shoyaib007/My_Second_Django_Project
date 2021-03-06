# Generated by Django 2.2.5 on 2021-01-25 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('instrument', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(blank=True, max_length=100)),
                ('release_date', models.DateField(null=True)),
                ('numstarts', models.IntegerField(choices=[(1, 'good'), (2, 'better'), (3, 'best')])),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Album_list', to='first_app.Musician')),
            ],
        ),
    ]
