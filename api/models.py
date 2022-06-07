from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

car_number_validators = [
    RegexValidator(r'^(01|10|20|25|30|40|50|60|70|75|80|85|90|95)[A-Z][0-9]{3}[A-Z]{2}$', "Qayta tekshiring. Kiritganingiz O'zbekiston avto raqami emas!"),
    RegexValidator(r'^(01|10|20|25|30|40|50|60|70|75|80|85|90|95)[0-9]{3}[A-Z]{3}$', "Qayta tekshiring. Kiritganingiz O'zbekiston avto raqami emas!")
]

wash_validators = [
    RegexValidator(r'^(accepted|pending|rejected)$', "Bazada xatolik. Status xato kiritildi.")
]

rating_validators = [
    RegexValidator(r'[0-9][0-9]', "Baho belgilangan chegaradan tashqarida qo'yildi.")
]

class Schedule(models.Model):
    Monday = models.BooleanField(default=False)
    Tuesday = models.BooleanField(default=False)
    Wednesday = models.BooleanField(default=False)
    Thursday = models.BooleanField(default=False)
    Friday = models.BooleanField(default=False)
    Saturday = models.BooleanField(default=False)
    Sunday = models.BooleanField(default=False)

class Car(models.Model):
    number = models.CharField(max_length=8, verbose_name='Mashina raqami', unique=True, validators=car_number_validators)
    owner = models.OneToOneField(verbose_name='Mashina egasi', to=User, on_delete=models.CASCADE)
    bot_number = models.IntegerField(verbose_name='Telefon raqam', null=True, blank=True, unique=True)
    registrated = models.DateTimeField(verbose_name="Ro'yxatdan o'tgan sana", null=False, blank=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Mashina'
        verbose_name_plural = 'Mashinalar'
        indexes = [
            models.Index(fields=['id']),
            models.Index(fields=['number'])
        ]

class CarWash(models.Model):
    name = models.CharField(max_length=25, verbose_name='Moyka nomi', null=False, blank=False, unique=True)
    bot_number = models.IntegerField(verbose_name='Telefon raqam', null=True, blank=True, unique=True)
    location = models.CharField(max_length=50, verbose_name='Manzil', null=False, blank=False)
    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(verbose_name='Bugungi narx')
    working_day = models.ForeignKey(verbose_name='Ish kunlari', to=Schedule, on_delete=models.CASCADE)
    working_hour_start = models.TimeField(verbose_name='Ochilish', null=False, blank=False)
    working_hour_end = models.TimeField(verbose_name='Yopilish', null=False, blank=False)
    registrated = models.DateTimeField(verbose_name="Ro'yxatdan o'tgan sana", null=False, blank=False, auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Oxirgi yangilangan sana", auto_now=True)

    class Meta:
        verbose_name = 'Moyka'
        verbose_name_plural = 'Moykalar'
        indexes = [
            models.Index(fields=['id']),
            models.Index(fields=['name']),
            models.Index(fields=['bot_number']),
        ]

class Discount(models.Model):
    washing_amount = models.IntegerField(verbose_name='Yuvishlar soni', null=False, blank=False)
    discount = models.IntegerField(verbose_name='Chegirma miqdori', null=False, blank=False)
    carwash = models.ForeignKey(CarWash, on_delete=models.CASCADE)
    created = models.DateTimeField(verbose_name="Yaratilgan sana", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Oxirgi yangilangan sana", auto_now=True)

    class Meta:
        verbose_name = 'Chegirma'
        verbose_name_plural = 'Chegirmalar'
        indexes = [
            models.Index(fields=['carwash']),
            models.Index(fields=['washing_amount']),
            models.Index(fields=['discount']),
        ]

class Wash(models.Model):
    carwash = models.ForeignKey(verbose_name="Moyka", to=CarWash, on_delete=models.PROTECT)
    car = models.ForeignKey(verbose_name='Mashina', to=Car, on_delete=models.PROTECT)
    created = models.DateTimeField(verbose_name='Yuvilgan vaqt', auto_now_add=True)
    price = models.IntegerField(verbose_name="Narx", null=False, blank=False)
    status = models.CharField(max_length=8, verbose_name='Status', validators=wash_validators)
    accepted = models.DateTimeField(verbose_name='Tasdiqlangan vaqt', null=True, blank=True)
    feedback = models.IntegerField(verbose_name="Baho", null=True, blank=True)