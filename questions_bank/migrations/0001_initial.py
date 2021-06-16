# Generated by Django 3.2.4 on 2021-06-15 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(default='', max_length=1000)),
                ('option', models.CharField(default='', max_length=100)),
                ('course_code', models.CharField(default='', max_length=10)),
                ('page_number', models.IntegerField(default=0)),
            ],
        ),
    ]
