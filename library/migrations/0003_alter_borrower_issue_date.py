# Generated by Django 4.0.5 on 2022-06-06 10:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_book_publish_date_alter_book_isbn_alter_book_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrower',
            name='issue_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name=datetime.date.today),
        ),
    ]