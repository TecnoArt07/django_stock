# Generated by Django 3.2.3 on 2021-06-03 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('quotes', '0003_delete_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=10)),
                ('user', models.CharField(default='guest', max_length=20)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
