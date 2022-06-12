from django import forms
from .models import Equipment, Plot, Accounting_for_failure, Reviewing_for_inspection, Users, Employee

class AddEquipment(forms.Form):
    type_equipment = forms.CharField(label="Тип оборудования")
    number_equipment = forms.IntegerField(label="Номер оборудования")
    name_equipment = forms.CharField(label="Название оборудования")

class AddPlots(forms.Form):
    number_plots = forms.IntegerField(label="Номер участка")
    name_plots = forms.CharField(label="Название участка")
    equipment_on_plots = forms.ModelChoiceField(label="Оборудование", queryset=Equipment.objects.all().order_by('id'))

class AddAccounting(forms.Form):
    date_of_accounting = forms.DateField(label="Дата отказа оборудования")
    reason_of_accounting = forms.CharField(label="Причина осмотра оборудования")
    equipment_of_accounting = forms.ModelChoiceField(label="Оборудование", queryset=Equipment.objects.all().order_by('id'))
    full_name_accounting_employee = forms.CharField(label="ФИО сотрудника")

class AddReviewing(forms.Form):
    date_of_reviewing = forms.DateField(label="Дата технического осмотра")
    result_of_reviewing = forms.CharField(label="Результат осмотра")
    reason_of_reviewing = forms.CharField(label="Причина осмотра")
    equipment_of_reviewing = forms.ModelChoiceField(label="Оборудование", queryset=Equipment.objects.all().order_by('id'))
    full_name_reviewing_employee = forms.CharField(label="ФИО сотрудника")

class AddUsers(forms.Form):
    number = forms.IntegerField(label="Номер пользователя")
    login = forms.CharField(label="Логин пользователя")
    password = forms.CharField(label="Пароль пользователя")

class AddEmployee(forms.Form):
    personal_number_employee = forms.IntegerField(label="Номер сотрудника")
    full_name_employee = forms.CharField(label="ФИО сотрудника")
    position_employee = forms.CharField(label="Должность сотрудника")
