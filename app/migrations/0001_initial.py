# Generated by Django 4.0.6 on 2022-09-28 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('mobile', models.CharField(max_length=12)),
                ('desc', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Wallpaper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('category', models.CharField(choices=[('N', 'Nature'), ('S', 'Space'), ('CO', 'Country'), ('A', 'Animal'), ('T', 'Tajmahal'), ('C', 'Car'), ('F', 'Flower'), ('W', 'Window'), ('CA', 'Cartoon'), ('M', 'Mobile'), ('TO', 'Top')], default=(('N', 'Nature'), ('S', 'Space'), ('CO', 'Country'), ('A', 'Animal'), ('T', 'Tajmahal'), ('C', 'Car'), ('F', 'Flower'), ('W', 'Window'), ('CA', 'Cartoon'), ('M', 'Mobile'), ('TO', 'Top')), max_length=5)),
                ('wallpaper_image', models.ImageField(upload_to='wallpaperimg')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
