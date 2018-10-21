# Generated by Django 2.1.2 on 2018-10-21 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='kabuka',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=4)),
                ('kjn_ymd', models.CharField(max_length=8)),
                ('hzm_ne', models.IntegerField()),
                ('tak_ne', models.IntegerField()),
                ('yas_ne', models.IntegerField()),
                ('owr_ne', models.IntegerField()),
                ('dekidaka', models.IntegerField()),
                ('chs_ne', models.IntegerField()),
                ('del_flg', models.CharField(default=0, max_length=1)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='kabuka',
            unique_together={('code', 'kjn_ymd')},
        ),
    ]