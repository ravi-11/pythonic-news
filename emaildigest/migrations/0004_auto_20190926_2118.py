# Generated by Django 2.2.5 on 2019-09-26 21:18

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('emaildigest', '0003_auto_20190923_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='UnSubscription',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('changed_at', models.DateTimeField(auto_now=True)),
                ('from_digest', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='emaildigest.EmailDigest')),
                ('subscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emaildigest.Subscription')),
            ],
        ),
    ]
