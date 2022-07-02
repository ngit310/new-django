from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AddEquipment, AddPlots, AddAccounting, AddReviewing, AddUsers, AddEmployee
from .models import Equipment, Plot, Accounting_for_failure, Reviewing_for_inspection, Users, Employee
from django.views import View
from django.http import HttpResponseRedirect
import pymysql

con = pymysql.connect(host='localhost',
                      user='root',
                      password='Qwerty777',
                      database='next_base')

auth_key = 0
user_id = 0

users_query = "SELECT login,password FROM firstapp_users"

res_users = []
with con.cursor() as cursor:
    cursor.execute(users_query)
    result = cursor.fetchall()

    for row in result:
        res_users.append([row[0], row[1]])

def index(request):
    global auth_key
    auth_key = 0
    return render(request, "DJApp\Template_Authorizated.html")

def auth(request):

    select_movies_query = "SELECT * FROM firstapp_users"
    global auth_key
    global user_id

    with con.cursor() as cursor:
        cursor.execute(select_movies_query)
        result = cursor.fetchall()

    if request.method == "POST":

        login_data = request.POST.get("login_in", "")
        pass_data = request.POST.get("password_in", "")

        for i in result:
            if (login_data == i[2] and pass_data == i[3]):
                user_id = i[0]
                auth_key = 1
                return HttpResponseRedirect("/main")

        auth_key = 0
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

def main_menu(request):

    global user_id
    global res_users
    global auth_key

    if auth_key == 1:

        person = "Unknown person"

        for i in res_users:
            if i[0] == user_id:
                person = i[1]

        return render(request, "DJApp\Template_Main.html", {"person":person})
    else:
        auth_key = 0
        return redirect('home')



# Equipment

def index_equipment(request):

    global user_id
    global res_users
    global auth_key

    person = "Unknown person"

    if auth_key == 0:
        return redirect('home')

    for i in res_users:
        if i[0] == user_id:
            person = i[1]

    form_ex = AddEquipment()
    data = Equipment.objects.all()
    return render(request, "DJApp\Template_Equipment.html", {"form":form_ex, "data_show":data, "person":person})

class view_equipment(View):

    def add_equipment(request):
        if request.method == "POST":
            new_data = Equipment()
            new_data.type_equipment = request.POST.get("type_equipment")
            new_data.number_equipment = request.POST.get("number_equipment")
            new_data.name_equipment = request.POST.get("name_equipment")
            new_data.save()
            return HttpResponseRedirect("/main/equipment")

    def del_equipment(request):
        if request.method == "POST":
            id_data = request.POST.get("delname", "")
            del_data = Equipment.objects.get(id_data)
            del_data.delete()
            return HttpResponseRedirect("/main/equipment")

    def update_equipment(request):
        if request.method == "POST":
            id_data = request.POST.get("upname", "")
            update_data = Equipment.objects.get(id_data)
            update_data.type_equipment = request.POST.get("type_equipment")
            update_data.number_equipment = request.POST.get("number_equipment")
            update_data.name_equipment = request.POST.get("name_equipment")
            update_data.save()
            return HttpResponseRedirect("/main/equipment")

# Plots

def index_plots(request):

    global user_id
    global res_users
    global auth_key

    person = "Unknown person"

    if auth_key == 0:
        return redirect('home')

    for i in res_users:
        if i[0] == user_id:
            person = i[1]

    form_ex = AddPlots()
    data = Plot.objects.all()
    return render(request, "DJApp\Template_Plots.html", {"form":form_ex, "data_show":data, "person":person})

class view_plots(View):

    def add_plots(request):
        if request.method == "POST":
            new_data = Plot()
            new_data.number_plots = request.POST.get("number_plots")
            new_data.name_plots = request.POST.get("name_plots")
            new_data.equipment_on_plots = Equipment.objects.get(request.POST.get("equipment_on_plots"))
            new_data.save()
            return HttpResponseRedirect("/main/plots")

    def del_plots(request):
        if request.method == "POST":
            id_data = request.POST.get("delname", "")
            del_data = Plot.objects.get(id_data)
            del_data.delete()
            return HttpResponseRedirect("/main/plots")

    def update_plots(request):
        if request.method == "POST":
            id_data = request.POST.get("upname", "")
            update_data = Plot.objects.get(id_data)
            update_data.number_plots = request.POST.get("number_plots")
            update_data.name_plots = request.POST.get("name_plots")
            update_data.equipment_on_plots = Equipment.objects.get(request.POST.get("equipment_on_plots"))
            update_data.save()
            return HttpResponseRedirect("/main/plots")

# Accounting

def index_acc(request):

    global user_id
    global res_users
    global auth_key

    person = "Unknown person"

    if auth_key == 0:
        return redirect('home')

    for i in res_users:
        if i[0] == user_id:
            person = i[1]

    form_ex = AddAccounting()
    data = Accounting_for_failure.objects.all()
    return render(request, "DJApp\Template_Accounting.html", {"form":form_ex, "data_show":data, "person":person})

class view_acc(View):

    def add_acc(request):
        if request.method == "POST":
            new_data = Accounting_for_failure()
            new_data.date_of_accounting = request.POST.get("date_of_accounting")
            new_data.reason_of_accounting = request.POST.get("reason_of_accounting")
            new_data.equipment_of_accounting = Equipment.objects.get(request.POST.get("equipment_of_accounting"))
            new_data.full_name_accounting_employee = request.POST.get("full_name_accounting_employee")
            new_data.save()
            return HttpResponseRedirect("/main/accounting")

    def del_acc(request):
        if request.method == "POST":
            id_data = request.POST.get("delname", "")
            del_data = Accounting_for_failure.objects.get(id_data)
            del_data.delete()
            return HttpResponseRedirect("/main/accounting")

    def update_acc(request):
        if request.method == "POST":
            id_data = request.POST.get("upname", "")
            update_data = Accounting_for_failure.objects.get(id_data)
            update_data.date_of_accounting = request.POST.get("date_Accounting")
            update_data.reason_of_accounting = request.POST.get("reason_Accounting")
            update_data.equipment_of_accounting = Equipment.objects.get(request.POST.get("equipment_id"))
            update_data.full_name_accounting_employee = request.POST.get("person_Accounting")
            update_data.save()
            return HttpResponseRedirect("/main/accounting")

# Reviewing

def index_review(request):

    global user_id
    global res_users
    global auth_key

    person = "Unknown person"

    if auth_key == 0:
        return redirect('home')

    for i in res_users:
        if i[0] == user_id:
            person = i[1]

    form_ex = AddReviewing()
    data = Reviewing_for_inspection.objects.all()
    return render(request, "DJApp\Template_Reviewing.html", {"form":form_ex, "data_show":data, "person":person})

class view_review(View):

    def add_review(request):
        if request.method == "POST":
            new_data = Reviewing_for_inspection()
            new_data.date_of_reviewing = request.POST.get("date_of_reviewing")
            new_data.result_of_reviewing = request.POST.get("result_of_reviewing")
            new_data.reason_of_reviewing = request.POST.get("reason_of_reviewing")
            new_data.equipment_of_reviewing = Equipment.objects.get(request.POST.get("equipment_of_reviewing"))
            new_data.full_name_reviewing_employee = request.POST.get("full_name_reviewing_employee")
            new_data.save()
            return HttpResponseRedirect("/main/reviewing")

    def del_review(request):
        if request.method == "POST":
            id_data = request.POST.get("delname", "")
            del_data = Reviewing_for_inspection.objects.get(id_data)
            del_data.delete()
            return HttpResponseRedirect("/main/reviewing")

    def update_review(request):
        if request.method == "POST":
            id_data = request.POST.get("upname", "")
            update_data = Reviewing_for_inspection.objects.get(id_data)
            update_data.date_of_reviewing = request.POST.get("date_of_reviewing")
            update_data.result_of_reviewing = request.POST.get("result_of_reviewing")
            update_data.reason_of_reviewing = request.POST.get("reason_of_reviewing")
            update_data.equipment_of_reviewing = Equipment.objects.get(request.POST.get("equipment_of_reviewing"))
            update_data.full_name_reviewing_employee = request.POST.get("full_name_reviewing_employee")
            update_data.save()
            return HttpResponseRedirect("/main/reviewing")

# Users

def index_users(request):

    global user_id
    global res_users
    global auth_key

    person = "Unknown person"

    if auth_key == 0:
        return redirect('home')

    for i in res_users:
        if i[0] == user_id:
            person = i[1]

    form_ex = AddUsers()
    data = Users.objects.all()
    return render(request, "DJApp\Template_Users.html", {"form":form_ex, "data_show":data, "person":person})

class view_users(View):

    def add_users(request):
        if request.method == "POST":
            new_data = Users()
            new_data.number = request.POST.get("number")
            new_data.login = request.POST.get("login")
            new_data.password = request.POST.get("password")
            new_data.save()
            return HttpResponseRedirect("/main/users")

    def del_users(request):
        if request.method == "POST":
            id_data = request.POST.get("delname", "")
            del_data = Users.objects.get(id_data)
            del_data.delete()
            return HttpResponseRedirect("/main/users")

    def update_users(request):
        if request.method == "POST":
            id_data = request.POST.get("upname", "")
            update_data = Users.objects.get(id_data)
            update_data.number = request.POST.get("number")
            update_data.login = request.POST.get("login")
            update_data.password = request.POST.get("password")
            update_data.save()
            return HttpResponseRedirect("/main/users")

# Employee

def index_employee(request):

    global user_id
    global res_users
    global auth_key

    person = "Unknown person"

    if auth_key == 0:
        return redirect('home')

    for i in res_users:
        if i[0] == user_id:
            person = i[1]

    form_ex = AddEmployee()
    data = Employee.objects.all()
    return render(request, "DJApp\Template_Employee.html", {"form":form_ex, "data_show":data, "person":person})

class view_employee(View):

    def add_employee(request):
        if request.method == "POST":
            new_data = Employee()
            new_data.personal_number_employee = request.POST.get("personal_number_employee")
            new_data.full_name_employee = request.POST.get("full_name_employee")
            new_data.position_employee = request.POST.get("position_employee")
            new_data.save()
            return HttpResponseRedirect("/main/employee")

    def del_employee(request):
        if request.method == "POST":
            id_data = request.POST.get("delname", "")
            del_data = Employee.objects.get(id_data)
            del_data.delete()
            return HttpResponseRedirect("/main/employee")

    def update_employee(request):
        if request.method == "POST":
            id_data = request.POST.get("upname", "")
            update_data = Employee.objects.get(id_data)
            update_data.personal_number_employee = request.POST.get("personal_number_employee")
            update_data.full_name_employee = request.POST.get("full_name_employee")
            update_data.position_employee = request.POST.get("position_employee")
            update_data.save()
            return HttpResponseRedirect("/main/employee")
