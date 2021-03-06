# Generated by Django 3.2.5 on 2021-08-05 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock_Name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('security_code', models.CharField(max_length=15)),
                ('issuer_name', models.CharField(db_index=True, max_length=150)),
                ('slug', models.SlugField(max_length=200)),
                ('security_id', models.CharField(max_length=50)),
                ('security_name', models.CharField(db_index=True, max_length=250)),
                ('status', models.BooleanField(default=True)),
                ('group', models.CharField(max_length=5)),
                ('face_value', models.IntegerField(default=0)),
                ('isin_no', models.CharField(max_length=20)),
                ('industry', models.CharField(max_length=100)),
                ('instrument', models.CharField(default='Equity', max_length=15)),
            ],
            options={
                'ordering': ('security_code',),
            },
        ),
    ]
