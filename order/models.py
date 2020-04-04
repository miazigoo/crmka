from django.conf import settings
from django.db import models
from django.utils import timezone 
from customer.models import Customer
from django import forms


class Shop(models.Model):
    servis_name = models.CharField(verbose_name="Магазин", max_length=70, db_index=True, blank=True)

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

    def __str__(self):
        return self.servis_name


class Status(models.Model):
    status_name = models.CharField(verbose_name="Статус готовности", max_length=70, db_index=True, blank=True)

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return self.status_name


class Post(models.Model):
	author = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Приёмщик")
	customer = models.ManyToManyField(Customer,verbose_name="Клиент", blank=True)
	shop = models.ForeignKey(Shop, related_name='shop', verbose_name="Магазин", on_delete=models.CASCADE, null=True)
	status = models.ForeignKey(Status, related_name='status', verbose_name="Статус", on_delete=models.CASCADE)
	model_Type = models.CharField(verbose_name="Тип модели", max_length=100, blank=True)
	firma = models.CharField(verbose_name="Фирма", max_length=50, blank=True)
	model_devie = models.CharField(verbose_name="Модель устройства",max_length=50, db_index=True, blank=True)
	Error_type = models.TextField(verbose_name="Тип поломки", blank=True)
	Cost = models.CharField(verbose_name="Стоимость",max_length=7)
	created_date = models.DateTimeField(auto_now_add=True)
	
	komplekt = models.CharField(verbose_name='Комплектация',max_length=200,blank=True)
	zametki_priemshika = models.CharField(verbose_name='Заметки приёмщика',max_length=200,blank=True)
	predoplata = models.CharField(verbose_name='Предопата',max_length=13,blank=True)
	
	def publish(self):
		self.save()

	