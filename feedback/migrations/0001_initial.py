# Generated by Django 5.2.4 on 2025-07-30 15:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('walktrails', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('location', models.TextField()),
                ('type', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=20)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('feedback_content', models.TextField()),
                ('feedback_image', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('in_progress', '처리중'), ('completed', '완료'), ('rejected', '반려')], default='in_progress', max_length=20)),
                ('response_content', models.TextField(blank=True, null=True)),
                ('responded_at', models.DateTimeField(blank=True, null=True)),
                ('response_image', models.TextField(blank=True, null=True)),
                ('admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='responses', to='accounts.admin')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedback', to='accounts.user')),
                ('walktrail', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='feedback', to='walktrails.walktrail')),
            ],
        ),
    ]
