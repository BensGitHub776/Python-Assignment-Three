# Generated by Django 5.1.1 on 2024-10-10 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_topic_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(blank=True, help_text='The date/time the article was published', null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', help_text='Set to published to make this publicly visible', max_length=10),
        ),
    ]