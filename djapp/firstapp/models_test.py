from django.db import models
import datetime
from django.test import TestCase
from .models import Equipment, Plot, Accounting_for_failure, Reviewing_for_inspection, Users, Employee
import unittest

class Equipment_dbModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Equipment.objects.create(({'date_of_reviewing': datetime.date.today, 'result_of_reviewing': "Результат", 'reason_of_reviewing': "Причина"
            ,'equipment_of_reviewing': 1, 'full_name_reviewing_employee': "ФИО сотрудника"}))

    #test 1 (label)

    def test_type_equipment_label(self):
        ad = Equipment.objects.get(1)
        field_label = ad._meta.get_field('type_equipment').verbose_name
        self.assertEquals(field_label, 'type_equipment')

    def test_number_equipment_label(self):
        ad = Equipment.objects.get(1)
        field_label = ad._meta.get_field('number_equipment').verbose_name
        self.assertEquals(field_label, 'number_equipment')

    def test_name_equipment_label(self):
        ad = Equipment.objects.get(1)
        field_label = ad._meta.get_field('name_equipment').verbose_name
        self.assertEquals(field_label, 'name_equipment')

    # test 2 (lenght)

    def test_type_equipment_length(self):
        ad = Equipment.objects.get(1)
        max_length = ad._meta.get_field('type_equipment').max_length
        self.assertEquals(max_length,120)

    def test_number_equipment_length(self):
        ad = Equipment.objects.get(1)
        max_length = ad._meta.get_field('number_equipment').max_length
        self.assertEquals(max_length,120)

    def test_name_equipment_length(self):
        ad = Equipment.objects.get(1)
        max_length = ad._meta.get_field('name_equipment').max_length
        self.assertEquals(max_length,120)

class Plot_dbModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Plot.objects.create(({'number_plots': 1, 'name_plots': "Имя", 'equipment_on_plots': 1}))

    # test 1 (label)

    def test_number_plots_label(self):
        ad = Plot.objects.get(1)
        field_label = ad._meta.get_field('number_plots').verbose_name
        self.assertEquals(field_label, 'number_plots')

    def test_name_plots_label(self):
        ad = Plot.objects.get(1)
        field_label = ad._meta.get_field('name_plots').verbose_name
        self.assertEquals(field_label, 'name_plots')

    def test_equipment_on_plots_label(self):
        ad = Plot.objects.get(1)
        field_label = ad._meta.get_field('equipment_on_plots').verbose_name
        self.assertEquals(field_label, 'equipment_on_plots')

    # test 2 (lenght)

    def test_number_plots_length(self):
        ad = Plot.objects.get(1)
        max_length = ad._meta.get_field('number_plots').max_length
        self.assertEquals(max_length, 120)

    def test_name_plots_length(self):
        ad = Plot.objects.get(1)
        max_length = ad._meta.get_field('name_plots').max_length
        self.assertEquals(max_length, 120)

    def test_equipment_on_plots_length(self):
        ad = Plot.objects.get(1)
        max_length = ad._meta.get_field('equipment_on_plots').max_length
        self.assertEquals(max_length, 120)

class Accounting_for_failure_dbModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Accounting_for_failure.objects.create(({'date_of_accounting': datetime.date.today, 'reason_of_accounting': "Причина", 'equipment_of_accounting': 1,
                                                'full_name_accounting_employee': "ФИО сотрудника"}))

    # test 1 (label)

    def test_date_of_accounting_label(self):
        ad = Accounting_for_failure.objects.get(1)
        field_label = ad._meta.get_field('date_of_accounting').verbose_name
        self.assertEquals(field_label, 'date_of_accounting')

    def test_reason_of_accounting_label(self):
        ad = Accounting_for_failure.objects.get(1)
        field_label = ad._meta.get_field('reason_of_accounting').verbose_name
        self.assertEquals(field_label, 'reason_of_accounting')

    def test_equipment_of_accounting_label(self):
        ad = Accounting_for_failure.objects.get(1)
        field_label = ad._meta.get_field('equipment_of_accounting').verbose_name
        self.assertEquals(field_label, 'equipment_of_accounting')

    def test_full_name_accounting_employee_label(self):
        ad = Accounting_for_failure.objects.get(1)
        field_label = ad._meta.get_field('full_name_accounting_employee').verbose_name
        self.assertEquals(field_label, 'full_name_accounting_employee')

    # test 2 (lenght)

    def test_date_of_accounting_length(self):
        ad = Accounting_for_failure.objects.get(1)
        max_length = ad._meta.get_field('date_of_accounting').max_length
        self.assertEquals(max_length, 120)

    def test_reason_of_accounting_length(self):
        ad = Accounting_for_failure.objects.get(1)
        max_length = ad._meta.get_field('reason_of_accounting').max_length
        self.assertEquals(max_length, 120)

    def test_equipment_of_accounting_length(self):
        ad = Accounting_for_failure.objects.get(1)
        max_length = ad._meta.get_field('equipment_of_accounting').max_length
        self.assertEquals(max_length, 120)

    def test_full_name_accounting_employee_length(self):
        ad = Accounting_for_failure.objects.get(1)
        max_length = ad._meta.get_field('full_name_accounting_employee').max_length
        self.assertEquals(max_length, 120)

class Reviewing_for_inspection_dbModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Reviewing_for_inspection.objects.create(({'date_of_reviewing': datetime.date.today,
                             'result_of_reviewing': "Результат", 'reason_of_reviewing': "Причина",'equipment_of_reviewing': 1, 'full_name_reviewing_employee': "ФИО сотрудника"}))

    # test 1 (label)

    def test_date_of_reviewing_label(self):
        ad = Reviewing_for_inspection.objects.get(1)
        field_label = ad._meta.get_field('date_of_reviewing').verbose_name
        self.assertEquals(field_label, 'date_of_reviewing')

    def test_result_of_reviewing_label(self):
        ad = Reviewing_for_inspection.objects.get(1)
        field_label = ad._meta.get_field('result_of_reviewing').verbose_name
        self.assertEquals(field_label, 'result_of_reviewing')

    def test_reason_of_reviewing_label(self):
        ad = Reviewing_for_inspection.objects.get(1)
        field_label = ad._meta.get_field('reason_of_reviewing').verbose_name
        self.assertEquals(field_label, 'reason_of_reviewing')

    def test_equipment_of_reviewing_label(self):
        ad = Reviewing_for_inspection.objects.get(1)
        field_label = ad._meta.get_field('equipment_of_reviewing').verbose_name
        self.assertEquals(field_label, 'equipment_of_reviewing')

    def test_full_name_reviewing_employee_label(self):
        ad = Reviewing_for_inspection.objects.get(1)
        field_label = ad._meta.get_field('full_name_reviewing_employee').verbose_name
        self.assertEquals(field_label, 'full_name_reviewing_employee')

    # test 2 (lenght)

    def test_date_of_reviewing_length(self):
        ad = Reviewing_for_inspection.objects.get(1)
        max_length = ad._meta.get_field('date_of_reviewing').max_length
        self.assertEquals(max_length, 120)

    def test_result_of_reviewing_length(self):
        ad = Reviewing_for_inspection.objects.get(1)
        max_length = ad._meta.get_field('result_of_reviewing').max_length
        self.assertEquals(max_length, 120)

    def test_reason_of_reviewing_length(self):
        ad = Reviewing_for_inspection.objects.get(1)
        max_length = ad._meta.get_field('reason_of_reviewing').max_length
        self.assertEquals(max_length, 120)

    def test_equipment_of_reviewing_length(self):
        ad = Reviewing_for_inspection.objects.get(1)
        max_length = ad._meta.get_field('equipment_of_reviewing').max_length
        self.assertEquals(max_length, 120)

    def test_full_name_reviewing_employee_length(self):
        ad = Reviewing_for_inspection.objects.get(1)
        max_length = ad._meta.get_field('full_name_reviewing_employee').max_length
        self.assertEquals(max_length, 120)

class Employee_dbModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Employee.objects.create(({'personal_number_employee': 1, 'full_name_employee': "ФИО сотрудника", 'position_employee': "Должность"}))

    #test 1 (label)

    def test_personal_number_employee_label(self):
        ad = Employee.objects.get(1)
        field_label = ad._meta.get_field('personal_number_employee').verbose_name
        self.assertEquals(field_label, 'personal_number_employee')

    def test_full_name_employee_label(self):
        ad = Employee.objects.get(1)
        field_label = ad._meta.get_field('full_name_employee').verbose_name
        self.assertEquals(field_label, 'full_name_employee')

    def test_position_employee_label(self):
        ad = Employee.objects.get(1)
        field_label = ad._meta.get_field('position_employee').verbose_name
        self.assertEquals(field_label, 'position_employee')

    # test 2 (lenght)

    def test_personal_number_employee_length(self):
        ad = Employee.objects.get(1)
        max_length = ad._meta.get_field('personal_number_employee').max_length
        self.assertEquals(max_length,120)

    def test_full_name_employee_length(self):
        ad = Employee.objects.get(1)
        max_length = ad._meta.get_field('full_name_employee').max_length
        self.assertEquals(max_length,120)

    def test_position_employee_length(self):
        ad = Employee.objects.get(1)
        max_length = ad._meta.get_field('position_employee').max_length
        self.assertEquals(max_length,120)

class Users_dbModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Users.objects.create(({'number': 1, 'login': "Логин", 'password': "Пароль"}))

    #test 1 (label)

    def test_number_label(self):
        ad = Users.objects.get(1)
        field_label = ad._meta.get_field('number').verbose_name
        self.assertEquals(field_label, 'number')

    def test_login_label(self):
        ad = Users.objects.get(1)
        field_label = ad._meta.get_field('login').verbose_name
        self.assertEquals(field_label, 'login')

    def test_password_label(self):
        ad = Users.objects.get(1)
        field_label = ad._meta.get_field('password').verbose_name
        self.assertEquals(field_label, 'password')

    # test 2 (lenght)

    def test_number_length(self):
        ad = Users.objects.get(1)
        max_length = ad._meta.get_field('number').max_length
        self.assertEquals(max_length,120)

    def test_login_length(self):
        ad = Users.objects.get(1)
        max_length = ad._meta.get_field('login').max_length
        self.assertEquals(max_length,120)

    def test_password_length(self):
        ad = Users.objects.get(1)
        max_length = ad._meta.get_field('password').max_length
        self.assertEquals(max_length,120)