# Generated by Django 4.1.2 on 2022-10-14 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaypalResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.JSONField(verbose_name='Paypal response')),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'PayPal response',
                'verbose_name_plural': 'PayPal responses',
            },
        ),
    ]
