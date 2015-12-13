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
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('apower', models.IntegerField(verbose_name='权限')),
                ('atime', models.DateTimeField(verbose_name='管理员创建时间')),
            ],
        ),
        migrations.CreateModel(
            name='Dgroup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('dname', models.CharField(max_length=32, verbose_name='大队名称')),
                ('daddr', models.CharField(max_length=32, verbose_name='大队地址')),
                ('dtime', models.DateTimeField(verbose_name='大队创建时间')),
            ],
        ),
        migrations.CreateModel(
            name='Fireinfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('fcar', models.IntegerField(verbose_name='出动车辆数')),
                ('fperson', models.IntegerField(verbose_name='出动人员数')),
                ('faddr', models.CharField(max_length=32, verbose_name='事故现场地址')),
                ('ftype', models.CharField(max_length=32, verbose_name='着火类型')),
                ('fmaterial', models.CharField(max_length=32, verbose_name='燃烧物质')),
                ('fhelptime', models.DateTimeField(verbose_name='救助时间')),
                ('finishtime', models.DateTimeField(verbose_name='结束时间')),
                ('fhelp', models.IntegerField(verbose_name='救助人数')),
                ('fhurt', models.IntegerField(verbose_name='受伤人数')),
                ('fdie', models.IntegerField(verbose_name='死亡人数')),
                ('farea', models.IntegerField(verbose_name='过火面积')),
                ('fmoney', models.IntegerField(verbose_name='损失金额（万元）')),
                ('fcontent', models.CharField(max_length=32, verbose_name='救助情况')),
                ('freason', models.CharField(max_length=32, verbose_name='事故原因')),
                ('ftime', models.DateTimeField(verbose_name='填表时间')),
            ],
        ),
        migrations.CreateModel(
            name='Reinforce',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('fcar', models.IntegerField(verbose_name='增援出动车辆数')),
                ('fperson', models.IntegerField(verbose_name='增援出动人员数')),
                ('rhelptime', models.DateTimeField(verbose_name='增援到长时间')),
                ('rfinishtime', models.DateTimeField(verbose_name='增援结束时间')),
                ('rtime', models.DateTimeField(verbose_name='填表时间')),
                ('fid', models.ForeignKey(to='frrs.Fireinfo', verbose_name='增援火场')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('uname', models.CharField(max_length=32, verbose_name='用户名')),
                ('upass', models.CharField(max_length=32, verbose_name='密码')),
                ('utime', models.DateTimeField(verbose_name='注册时间')),
                ('did', models.ForeignKey(to='frrs.Dgroup')),
            ],
        ),
        migrations.CreateModel(
            name='Zgroup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('zname', models.CharField(max_length=32, verbose_name='中队名称')),
                ('zaddr', models.CharField(max_length=32, verbose_name='中队地址')),
                ('ztime', models.DateTimeField(verbose_name='中队创建时间')),
                ('did', models.ForeignKey(to='frrs.Dgroup')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='zid',
            field=models.ForeignKey(to='frrs.Zgroup'),
        ),
        migrations.AddField(
            model_name='reinforce',
            name='zid',
            field=models.ForeignKey(to='frrs.Zgroup', verbose_name='增援中队'),
        ),
        migrations.AddField(
            model_name='fireinfo',
            name='zid',
            field=models.ForeignKey(to='frrs.Zgroup', verbose_name='主战中队'),
        ),
        migrations.AddField(
            model_name='admin',
            name='uid',
            field=models.ForeignKey(to='frrs.User'),
        ),
    ]
