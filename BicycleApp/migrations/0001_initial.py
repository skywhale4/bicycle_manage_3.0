# Generated by Django 4.0.4 on 2022-05-28 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('adminid', models.AutoField(primary_key=True, serialize=False)),
                ('adminname', models.CharField(max_length=50, unique=True)),
                ('adminpwd', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Bicycle',
            fields=[
                ('carid', models.AutoField(primary_key=True, serialize=False)),
                ('carbrand', models.CharField(max_length=50)),
                ('layplace', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('carid', models.IntegerField()),
                ('borrowtime', models.DateTimeField()),
                ('returntime', models.DateTimeField(null=True)),
                ('borrowplace', models.CharField(max_length=50)),
                ('returnplace', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('userpwd', models.CharField(max_length=50)),
                ('regtime', models.DateTimeField()),
                ('logtime', models.DateTimeField(null=True)),
            ],
        ),
    ]
