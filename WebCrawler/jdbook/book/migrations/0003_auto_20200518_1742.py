# Generated by Django 2.1.8 on 2020-05-18 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20200512_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinfo',
            name='store',
            field=models.CharField(default='无', max_length=100, null=True, verbose_name='出版社'),
        ),
    ]
