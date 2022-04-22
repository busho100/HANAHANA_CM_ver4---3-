# Generated by Django 4.0.3 on 2022-04-19 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_no', models.CharField(max_length=8)),
                ('adress', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CareManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cm_name', models.CharField(max_length=50)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Riyousha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hihoken_no', models.BigIntegerField()),
                ('name', models.CharField(max_length=50)),
                ('name_kana', models.CharField(max_length=100)),
                ('nyuuryoku_date', models.DateField()),
                ('sex', models.BooleanField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Riyousha_kihon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hana_cm.adress')),
                ('caremanager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hana_cm.caremanager')),
                ('riyousha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hana_cm.riyousha')),
            ],
        ),
        migrations.AddField(
            model_name='caremanager',
            name='riyousha',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cm_riyousha', to='hana_cm.riyousha'),
        ),
        migrations.AddField(
            model_name='adress',
            name='riyousha',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adress_riyousha', to='hana_cm.riyousha'),
        ),
        migrations.CreateModel(
            name='Adl_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nyuuryoku_date', models.DateField()),
                ('non', models.BooleanField(help_text='「なし」なら、チェックしてください')),
                ('left_upper_limbs', models.BooleanField(choices=[(False, 'なし'), (True, 'あり')], help_text='「左上肢に麻痺」があれば、チェックしてください')),
                ('left_lower_limbs', models.BooleanField(choices=[(False, 'なし'), (True, 'あり')], help_text='「左下肢に麻痺」があれば、チェックしてください')),
                ('right_upper_limbs', models.BooleanField(choices=[(False, 'なし'), (True, 'あり')], help_text='「右上肢に麻痺」があれば、チェックしてください')),
                ('right_lower_limbs', models.BooleanField(choices=[(False, 'なし'), (True, 'あり')], help_text='「右下肢に麻痺」があれば、チェックしてください')),
                ('others', models.BooleanField(help_text='「その他」があれば、チェックしてください。詳細を「麻痺その他」に記入してください')),
                ('paralysis_others', models.CharField(max_length=50)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('riyousha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hana_cm.riyousha')),
            ],
        ),
    ]
