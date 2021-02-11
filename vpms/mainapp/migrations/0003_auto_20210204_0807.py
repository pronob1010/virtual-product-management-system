# Generated by Django 3.1.6 on 2021-02-04 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20210204_0408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='card_description',
            field=models.TextField(blank=True, default=None, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='card_tittle',
            field=models.CharField(default=None, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='card_used',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='Gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender')], default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(blank=True, default=None, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='self_bio',
            field=models.TextField(blank=True, default=None, max_length=150, null=True),
        ),
    ]
