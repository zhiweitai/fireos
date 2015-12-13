# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('apower', models.IntegerField(verbose_name='权限')),
                ('atime', models.DateTimeField(verbose_name='管理员创建时间')),
            ],
        ),
        migrations.CreateModel(
            name='Dgroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('dname', models.CharField(verbose_name='大队名称', max_length=32)),
                ('daddr', models.CharField(verbose_name='大队地址', max_length=32)),
                ('dtime', models.DateTimeField(verbose_name='大队创建时间')),
            ],
        ),
        migrations.CreateModel(
            name='Fireinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('fcar', models.IntegerField(verbose_name='出动车辆数')),
                ('fperson', models.IntegerField(verbose_name='出动人员数')),
                ('faddr', models.CharField(verbose_name='事故现场地址', max_length=32)),
                ('ftype', models.CharField(verbose_name='着火类型', max_length=32)),
                ('fmaterial', models.CharField(verbose_name='燃烧物质', max_length=32)),
                ('fhelptime', models.DateTimeField(verbose_name='救助时间')),
                ('finishtime', models.DateTimeField(verbose_name='结束时间')),
                ('fhelp', models.IntegerField(verbose_name='救助人数')),
                ('fhurt', models.IntegerField(verbose_name='受伤人数')),
                ('fdie', models.IntegerField(verbose_name='死亡人数')),
                ('farea', models.IntegerField(verbose_name='过火面积')),
                ('fmoney', models.IntegerField(verbose_name='损失金额（万元）')),
                ('fcontent', models.CharField(verbose_name='救助情况', max_length=32)),
                ('freason', models.CharField(verbose_name='事故原因', max_length=32)),
                ('ftime', models.DateTimeField(verbose_name='填表时间')),
            ],
        ),
        migrations.CreateModel(
            name='Reinforce',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('fcar', models.IntegerField(verbose_name='增援出动车辆数')),
                ('fperson', models.IntegerField(verbose_name='增援出动人员数')),
                ('rhelptime', models.DateTimeField(verbose_name='增援到长时间')),
                ('rfinishtime', models.DateTimeField(verbose_name='增援结束时间')),
                ('rtime', models.DateTimeField(verbose_name='填表时间')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('uname', models.CharField(verbose_name='用户名', max_length=32)),
                ('upass', models.CharField(verbose_name='密码', max_length=32)),
                ('utime', models.DateTimeField(verbose_name='注册时间')),
                ('did', models.ForeignKey(to='frrs.Dgroup', verbose_name='大队外键')),
            ],
        ),
        migrations.CreateModel(
            name='Zgroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('zname', models.CharField(verbose_name='中队名称', max_length=32)),
                ('zaddr', models.CharField(verbose_name='中队地址', max_length=32)),
                ('ztime', models.DateTimeField(verbose_name='中队创建时间')),
                ('did', models.ForeignKey(to='frrs.Dgroup')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='zid',
            field=models.ForeignKey(to='frrs.Zgroup', verbose_name='中队外键'),
        ),
        migrations.AddField(
            model_name='reinforce',
            name='zid',
            field=models.ForeignKey(to='frrs.Zgroup'),
        ),
        migrations.AddField(
            model_name='fireinfo',
            name='rid',
            field=models.ForeignKey(to='frrs.Reinforce', verbose_name='增援外键'),
        ),
        migrations.AddField(
            model_name='fireinfo',
            name='zid',
            field=models.ForeignKey(to='frrs.Zgroup', verbose_name='中队外键'),
        ),
        migrations.AddField(
            model_name='admin',
            name='uid',
            field=models.ForeignKey(to='frrs.User'),
        ),
    ]
