# Generated by Django 2.2 on 2021-03-27 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_grpc_framework', '0010_auto_20210326_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='sociogrpcerrors',
            name='aborted',
            field=models.BooleanField(default=False, verbose_name='Thread aborted ?'),
        ),
        migrations.AddField(
            model_name='sociogrpcerrors',
            name='database',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='django_grpc_framework.grcpDataBases', verbose_name='Database Microservice'),
        ),
        migrations.AddField(
            model_name='sociogrpcerrors',
            name='error',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='django_grpc_framework.grcpErrorCode', verbose_name='Microservice Error'),
        ),
        migrations.AddField(
            model_name='sociogrpcerrors',
            name='query',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='sociogrpcerrors',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='django_grpc_framework.grcpMicroServices', verbose_name='Socotec Microservice'),
        ),
        migrations.AlterField(
            model_name='sociogrpcerrors',
            name='call_type',
            field=models.IntegerField(choices=[(1, 'List'), (2, 'Create'), (3, 'Retrieve'), (4, 'Update'), (5, 'Destroy')], default=0),
        ),
        migrations.CreateModel(
            name='grcpProtoBuf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True)),
                ('modified', models.DateTimeField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('protobuf', models.CharField(db_index=True, default='', max_length=50, verbose_name='Proto Name')),
                ('file', models.CharField(db_index=True, default='', max_length=50, verbose_name='Proto File')),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='django_grpc_framework.grcpDataBases', verbose_name='Microservice Database')),
            ],
            options={
                'verbose_name': 'GRPC PROTOBUF',
                'verbose_name_plural': 'GRPC PROTOBUF',
            },
        ),
    ]
