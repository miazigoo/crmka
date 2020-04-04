from django.db import models
from django.conf import settings
from order.models import *


class Customer(models.Model):
	"""docstring for Customer"""
	customer_name = models.CharField(verbose_name="Имя Клиента",max_length=28, db_index=True, blank=True, null=True)
	customer_surname = models.CharField(verbose_name="Фамилия Клиента",max_length=28, db_index=True, blank=True, null=True)
	customer_patronymic = models.CharField(verbose_name="Отчество Клиента",max_length=28, db_index=True, blank=True, null=True)
	customer_phone = models.IntegerField(verbose_name='Номер Клиента', db_index=True, blank=True, null=True)
	uznali_o_nas = models.CharField(verbose_name='Узнали о нас ', max_length=48, blank=True, null=True)

	class Meta:
		verbose_name='Клиент'
		verbose_name_plural = 'Клиенты'

	def __str__(self):
		return self.customer_surname
		