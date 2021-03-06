# Generated by Django 2.2.1 on 2019-05-21 09:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categori',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('c_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('states', models.CharField(choices=[('1', 'Bangladesh'), ('2', 'India'), ('3', 'Mayanmar'), ('4', 'Soudi Arabia'), ('5', 'Pakistan'), ('6', 'Canada'), ('7', 'Malaysia'), ('8', 'China'), ('9', 'US'), ('10', 'UK'), ('11', 'Other')], max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('town', models.CharField(max_length=200)),
                ('zipcode', models.PositiveIntegerField()),
                ('phone_number', models.IntegerField()),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('image', models.ImageField(upload_to='media/home')),
                ('details', models.TextField()),
                ('posted_on', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('image', models.ImageField(upload_to='media/shop')),
                ('details', models.TextField()),
                ('posted_on', models.DateTimeField(blank=True, null=True)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Basic_App.home')),
            ],
        ),
    ]
