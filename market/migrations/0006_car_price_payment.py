# Generated by Django 4.1.5 on 2023-02-18 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0005_purchase'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('date', models.DateField(auto_now_add=True)),
                ('credit_card', models.CharField(max_length=30)),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.order')),
            ],
        ),
    ]
