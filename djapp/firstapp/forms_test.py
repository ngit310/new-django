from django.test import TestCase
import unittest
import datetime
from django import forms
from .forms import AddEquipment, AddPlots, AddAccounting, AddReviewing, AddUsers, AddEmployee, Accounting_for_failure
from .models import Equipment, Plot, Accounting_for_failure, Reviewing_for_inspection, Users, Employee

class AddEquipmentFormTest(TestCase):

    def test_type_equipment(self):
        form = AddEquipment()
        self.assertTrue(form.fields['type_equipment'].label == None or form.fields['type_equipment'].label == 'Тип оборудования')

    def test_number_equipment(self):
        form = AddEquipment()
        self.assertTrue(form.fields['number_equipment'].label == None or form.fields['number_equipment'].label == 'Номер оборудования')

    def test_name_equipment(self):
        form = AddEquipment()
        self.assertTrue(form.fields['name_equipment'].label == None or form.fields['name_equipment'].label == 'Название оборудования')

    def test_resoult(self):
        form = AddEquipment({'type_equipment': "Тип", 'number_equipment': 1, 'name_equipment': 'Имя'})
        self.assertTrue(form.is_valid())

class AddPlotsFormTest(TestCase):

    def test_number_plots(self):
        form = AddPlots()
        self.assertTrue(form.fields['number_plots'].label == None or form.fields['number_plots'].label == 'Номер участка')

    def test_name_plots(self):
        form = AddPlots()
        self.assertTrue(form.fields['name_plots'].label == None or form.fields['name_plots'].label == 'Название участка')

    def test_equipment_on_plots(self):
        form = AddPlots()
        self.assertTrue(form.fields['equipment_on_plots'].label == None or form.fields['equipment_on_plots'].label == 'Оборудование')

    def test_resoult(self):
        form = AddPlots({'number_plots': 1, 'name_plots': "Имя", 'equipment_on_plots': 1})
        self.assertTrue(form.is_valid())

class AddAccountingFormTest(TestCase):

    def test_date_of_accounting(self):
        form = AddAccounting()
        self.assertTrue(form.fields['date_of_accounting'].label == None or form.fields['date_of_accounting'].label == 'Дата отказа оборудования')

    def test_reason_of_accounting(self):
        form = AddAccounting()
        self.assertTrue(form.fields['reason_of_accounting'].label == None or form.fields['reason_of_accounting'].label == 'Причина осмотра оборудования')

    def test_equipment_of_accounting(self):
        form = AddAccounting()
        self.assertTrue(form.fields['equipment_of_accounting'].label == None or form.fields['equipment_of_accounting'].label == 'Оборудование')

    def test_full_name_accounting_employee(self):
        form = AddAccounting()
        self.assertTrue(form.fields['full_name_accounting_employee'].label == None or form.fields['full_name_accounting_employee'].label == 'ФИО сотрудника')

    def test_resoult(self):
        form = AddAccounting({'date_of_accounting': datetime.date.today, 'reason_of_accounting': "Причина", 'equipment_of_accounting': 1, 'full_name_accounting_employee': "ФИО сотрудника"})
        self.assertTrue(form.is_valid())

class AddReviewingFormTest(TestCase):

    def test_date_of_reviewing(self):
        form = AddReviewing()
        self.assertTrue(form.fields['date_of_reviewing'].label == None or form.fields['date_of_reviewing'].label == 'Дата технического осмотра')

    def test_result_of_reviewing(self):
        form = AddReviewing()
        self.assertTrue(form.fields['result_of_reviewing'].label == None or form.fields['result_of_reviewing'].label == 'Результат осмотра')

    def test_reason_of_reviewing(self):
        form = AddReviewing()
        self.assertTrue(form.fields['reason_of_reviewing'].label == None or form.fields['reason_of_reviewing'].label == 'Причина осмотра')

    def test_equipment_of_reviewing(self):
        form = AddAccounting()
        self.assertTrue(form.fields['equipment_of_reviewing'].label == None or form.fields['equipment_of_reviewing'].label == 'Оборудование')

    def test_full_name_reviewing_employee(self):
        form = AddReviewing()
        self.assertTrue(form.fields['full_name_reviewing_employee'].label == None or form.fields['full_name_reviewing_employee'].label == 'ФИО сотрудника')

    def test_resoult(self):
        form = AddReviewing({'date_of_reviewing': datetime.date.today,
                             'result_of_reviewing': "Результат", 'reason_of_reviewing': "Причина",'equipment_of_reviewing': 1, 'full_name_reviewing_employee': "ФИО сотрудника"})
        self.assertTrue(form.is_valid())

class AddUsersFormTest(TestCase):

    def test_number(self):
        form = AddUsers()
        self.assertTrue(form.fields['number'].label == None or form.fields['number'].label == 'Номер пользователя')

    def test_login(self):
        form = AddUsers()
        self.assertTrue(form.fields['login'].label == None or form.fields['login'].label == 'Логин пользователя')

    def test_password(self):
        form = AddUsers()
        self.assertTrue(form.fields['password'].label == None or form.fields['password'].label == 'Пароль пользователя')

    def test_resoult(self):
        form = AddUsers({'number': 1, 'login': "Логин", 'password': "Пароль"})
        self.assertTrue(form.is_valid())

class AddEmployeeFormTest(TestCase):

    def test_personal_number_employee(self):
        form = AddEmployee()
        self.assertTrue(form.fields['personal_number_employee'].label == None or form.fields['personal_number_employee'].label == 'Номер сотрудника')

    def test_full_name_employee(self):
        form = AddEmployee()
        self.assertTrue(form.fields['full_name_employee'].label == None or form.fields['full_name_employee'].label == 'ФИО сотрудника')

    def test_position_employee(self):
        form = AddEmployee()
        self.assertTrue(form.fields['position_employee'].label == None or form.fields['position_employee'].label == 'Должность сотрудника')

    def test_resoult(self):
        form = AddEmployee({'personal_number_employee': 1, 'full_name_employee': "ФИО сотрудника", 'position_employee': "Должность"})
        self.assertTrue(form.is_valid())

