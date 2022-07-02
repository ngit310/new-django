from datetime import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from .forms import AddEquipment, AddPlots, AddAccounting, AddReviewing, AddUsers, AddEmployee
from .models import Equipment, Plot, Accounting_for_failure, Reviewing_for_inspection, Users, Employee
from django.views import View
from django.test import TestCase
import unittest
from django.http import HttpResponseRedirect
import pymysql

class view_equipment_Test(TestCase):

    @classmethod
    def setUpTestData(cls):
        Equipment.objects.create({'date_of_reviewing': datetime.date.today, 'result_of_reviewing': "Результат", 'reason_of_reviewing': "Причина"
            ,'equipment_of_reviewing': 1, 'full_name_reviewing_employee': "ФИО сотрудника"})

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/equipment/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('equipment'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('equipment'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'firstapp/Template_Equipment.html')

class view_plots_Test(TestCase):

    @classmethod
    def setUpTestData(cls):
        Plot.objects.create({'number_plots': 1, 'name_plots': "Имя", 'equipment_on_plots': 1})

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/plots/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('plots'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('plots'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'firstapp/Template_Plots.html')

class view_acc_Test(TestCase):

    @classmethod
    def setUpTestData(cls):
        Accounting_for_failure.objects.create({'date_of_accounting': datetime.date.today, 'reason_of_accounting': "Причина", 'equipment_of_accounting': 1,
                                                'full_name_accounting_employee': "ФИО сотрудника"})

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/accounting/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('accounting'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('plots'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'firstapp/Template_Accounting.html')

class view_review_Test(TestCase):

    @classmethod
    def setUpTestData(cls):
        Reviewing_for_inspection.objects.create({'date_of_reviewing': datetime.date.today,
                             'result_of_reviewing': "Результат", 'reason_of_reviewing': "Причина",'equipment_of_reviewing': 1, 'full_name_reviewing_employee': "ФИО сотрудника"})

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/reviewing/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('reviewing'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('plots'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'firstapp/Template_Reviewing.html')

class view_users_Test(TestCase):

    @classmethod
    def setUpTestData(cls):
        Users.objects.create({'number': 1, 'login': "Логин", 'password': "Пароль"})

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/users/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('users'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('plots'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'firstapp/Template_Users.html')

class view_employee_Test(TestCase):

    @classmethod
    def setUpTestData(cls):
        Employee.objects.create({'personal_number_employee': 1, 'full_name_employee': "ФИО сотрудника", 'position_employee': "Должность"})

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/employee/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('employee'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('plots'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'firstapp/Template_Employee.html')

