# Generated by Django 4.0.5 on 2022-06-07 04:17

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=8, unique=True, validators=[django.core.validators.RegexValidator('^(01|10|20|25|30|40|50|60|70|75|80|85|90|95)[A-Z][0-9]{3}[A-Z]{2}$', "Qayta tekshiring. Kiritganingiz O'zbekiston avto raqami emas!"), django.core.validators.RegexValidator('^(01|10|20|25|30|40|50|60|70|75|80|85|90|95)[0-9]{3}[A-Z]{3}$', "Qayta tekshiring. Kiritganingiz O'zbekiston avto raqami emas!")], verbose_name='Mashina raqami')),
                ('bot_number', models.IntegerField(blank=True, null=True, unique=True, verbose_name='Telefon raqam')),
                ('registrated', models.DateTimeField(auto_now_add=True, verbose_name="Ro'yxatdan o'tgan sana")),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Mashina egasi')),
            ],
            options={
                'verbose_name': 'Mashina',
                'verbose_name_plural': 'Mashinalar',
            },
        ),
        migrations.CreateModel(
            name='CarWash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True, verbose_name='Moyka nomi')),
                ('bot_number', models.IntegerField(blank=True, null=True, unique=True, verbose_name='Telefon raqam')),
                ('location', models.CharField(max_length=50, verbose_name='Manzil')),
                ('latitude', models.IntegerField(blank=True, null=True)),
                ('longitude', models.IntegerField(blank=True, null=True)),
                ('price', models.IntegerField(verbose_name='Bugungi narx')),
                ('working_hour_start', models.TimeField(verbose_name='Ochilish')),
                ('working_hour_end', models.TimeField(verbose_name='Yopilish')),
                ('registrated', models.DateTimeField(auto_now_add=True, verbose_name="Ro'yxatdan o'tgan sana")),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Oxirgi yangilangan sana')),
            ],
            options={
                'verbose_name': 'Moyka',
                'verbose_name_plural': 'Moykalar',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Monday', models.BooleanField(default=False)),
                ('Tuesday', models.BooleanField(default=False)),
                ('Wednesday', models.BooleanField(default=False)),
                ('Thursday', models.BooleanField(default=False)),
                ('Friday', models.BooleanField(default=False)),
                ('Saturday', models.BooleanField(default=False)),
                ('Sunday', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Wash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Yuvilgan vaqt')),
                ('price', models.IntegerField(verbose_name='Narx')),
                ('status', models.CharField(max_length=8, validators=[django.core.validators.RegexValidator('^(accepted|pending|rejected)$', 'Bazada xatolik. Status xato kiritildi.')], verbose_name='Status')),
                ('accepted', models.DateTimeField(blank=True, null=True, verbose_name='Tasdiqlangan vaqt')),
                ('feedback', models.IntegerField(blank=True, null=True, verbose_name='Baho')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.car', verbose_name='Mashina')),
                ('carwash', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.carwash', verbose_name='Moyka')),
            ],
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('washing_amount', models.IntegerField(verbose_name='Yuvishlar soni')),
                ('discount', models.IntegerField(verbose_name='Chegirma miqdori')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan sana')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Oxirgi yangilangan sana')),
                ('carwash', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.carwash')),
            ],
            options={
                'verbose_name': 'Chegirma',
                'verbose_name_plural': 'Chegirmalar',
            },
        ),
        migrations.AddField(
            model_name='carwash',
            name='working_day',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.schedule', verbose_name='Ish kunlari'),
        ),
        migrations.AddIndex(
            model_name='discount',
            index=models.Index(fields=['carwash'], name='api_discoun_carwash_20cdd7_idx'),
        ),
        migrations.AddIndex(
            model_name='discount',
            index=models.Index(fields=['washing_amount'], name='api_discoun_washing_ff30ea_idx'),
        ),
        migrations.AddIndex(
            model_name='discount',
            index=models.Index(fields=['discount'], name='api_discoun_discoun_ed68dd_idx'),
        ),
        migrations.AddIndex(
            model_name='carwash',
            index=models.Index(fields=['id'], name='api_carwash_id_87fb16_idx'),
        ),
        migrations.AddIndex(
            model_name='carwash',
            index=models.Index(fields=['name'], name='api_carwash_name_78166a_idx'),
        ),
        migrations.AddIndex(
            model_name='carwash',
            index=models.Index(fields=['bot_number'], name='api_carwash_bot_num_5d2808_idx'),
        ),
        migrations.AddIndex(
            model_name='car',
            index=models.Index(fields=['id'], name='api_car_id_8e4be1_idx'),
        ),
        migrations.AddIndex(
            model_name='car',
            index=models.Index(fields=['number'], name='api_car_number_bb0558_idx'),
        ),
    ]
