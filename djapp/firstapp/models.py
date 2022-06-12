from django.db import models
import datetime

# (Исправлено) - оборудование
class Equipment(models.Model):

    type_equipment = models.CharField(max_length=120, blank=True)
    number_equipment = models.IntegerField()
    name_equipment = models.CharField(max_length=120, blank=True)
    objects = models.Manager()

# (Исправлено) - участок
class Plot(models.Model):

    number_plots = models.IntegerField()
    name_plots = models.CharField(max_length=120)
    equipment_on_plots = models.ForeignKey('Equipment', on_delete=models.CASCADE)
    objects = models.Manager()

# (Исправлено) - учёт отказа оборудования
class Accounting_for_failure(models.Model):

    date_of_accounting = models.DateField(default=datetime.date.today)
    reason_of_accounting = models.CharField(max_length=120)
    equipment_of_accounting = models.ForeignKey('Equipment', on_delete=models.CASCADE)
    full_name_accounting_employee = models.CharField(max_length=120)
    objects = models.Manager()

# (Исправлено) - учёт технического осмотра
class Reviewing_for_inspection(models.Model):

    date_of_reviewing = models.DateField(default=datetime.date.today)
    result_of_reviewing = models.CharField(max_length=120)
    reason_of_reviewing = models.CharField(max_length=120)
    equipment_of_reviewing = models.ForeignKey('Equipment', on_delete=models.CASCADE)
    full_name_reviewing_employee = models.CharField(max_length=120)
    objects = models.Manager()

# (Исправлено) - сотрудники предприятия
class Employee(models.Model):

    personal_number_employee = models.IntegerField()
    full_name_employee = models.CharField(max_length=120)
    position_employee = models.CharField(max_length=120)
    objects = models.Manager()

class Users(models.Model):

    number = models.IntegerField()
    login = models.CharField(max_length=120)
    password = models.CharField(max_length=120)
    objects = models.Manager()

