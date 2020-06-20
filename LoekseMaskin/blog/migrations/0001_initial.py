# Generated by Django 3.0.2 on 2020-06-20 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(default='Tittel', max_length=20)),
                ('leadParagraph', models.CharField(default='Ingress', max_length=200)),
                ('article', models.CharField(default='Artikkel', max_length=2000)),
                ('publishedDate', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Vaskelister',
            },
        ),
    ]
