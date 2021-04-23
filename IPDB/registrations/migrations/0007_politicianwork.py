# Generated by Django 3.1.7 on 2021-04-23 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0006_auto_20210423_2329'),
    ]

    operations = [
        migrations.CreateModel(
            name='PoliticianWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(default='0')),
                ('work', models.CharField(max_length=1000)),
                ('politician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='worlRatings', to='registrations.politicians')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workUser', to='registrations.useraccounts', unique=True)),
            ],
        ),
    ]
