# Generated by Django 2.1 on 2020-07-30 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0003_topic_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name': '条目', 'verbose_name_plural': '条目'},
        ),
        migrations.AlterModelOptions(
            name='topic',
            options={'verbose_name': '主题', 'verbose_name_plural': '主题'},
        ),
    ]