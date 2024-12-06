from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django_daraja.mpesa.core import MpesaClient
from rest_framework import status
from rest_framework.decorators import api_view

from application.forms import StudentForm, LoginForm, MonthlyPackageForm, \
    HalfPackageForm, YearlyPackageForm, NewAdminForm
from application.models import Student, MonthlyPackage, HalfPackage, YearlyPackage
from application.serializers import StudentSerializer


# Create your views here.
def index(request):
    return render(request, 'index.html')

# registering to saving to database

def register(request):
    if request.method == 'POST':

        form = StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = StudentForm()
    return render(request, 'register.html', {"form": form})

def login(request):
    if request.method == 'POST':

        form = LoginForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'login.html', {"form": form})



def new_admin(request):
    if request.method == 'POST':
        form = NewAdminForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have registered a new admin')
            return redirect('new_admin')
    else:
            form = NewAdminForm()

    return render(request, 'new_admins.html', {"form": form})

#
#
#
# admin server side

def members(request):
    data = Student.objects.all()
    monthly_data = MonthlyPackage.objects.all()
    half_data = HalfPackage.objects.all()
    yearly_data = YearlyPackage.objects.all()
    return render(request, 'members.html',{
        "data":data,
        "monthly_data":monthly_data,
        "half_data":half_data,
        "yearly_data":yearly_data
    })

def admin_classes(request):
    return render(request, 'admin_classes.html')

# registering to class in database

def monthly_package(request):
    if request.method == 'POST':
        form = MonthlyPackageForm( request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = MonthlyPackageForm()
    return render(request, 'register_monthly_package.html', {"form": form})

def half_package(request):
    if request.method == 'POST':
        form = HalfPackageForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('index')
    else:
        form = HalfPackageForm()
    return render(request, 'register_half_package.html', {"form": form})

def yearly_package(request):
    if request.method == 'POST':
        form = YearlyPackageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = YearlyPackageForm()
    return render(request, 'register_yearly_package.html', {"form": form})


# mapping student from id is unique from one record(student) to another
def edit(request,id):
    # fetching model Student
    # store in variable student
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        # instance is already existing values pre-existing values
        # make changes
        form = StudentForm(request.POST,request.FILES ,instance = student)
        # if valid display or not valid
        if form.is_valid():
            form.save()
            messages.success(request, 'student updated successfully')
            # when click on update it returns you to members page
            return redirect('members')
        else:
            messages.error(request, 'please check form details')
    # if not POST check on GET
    # GET means we populate the form with existing details in the database
    else:
        form = StudentForm(instance=student)
    return render(request, 'edit.html', {"form": form, 'student': student})

# mapping a specific object from the model i created student
def delete(request,id):
    student = get_object_or_404(Student, id=id)
    # try catch
    # delete the student with id selected
    try:
        student.delete()
        messages.success(request, 'student deleted successfully')
    except Exception as e:
        messages.error(request, 'message not deleted')

    return redirect('members')



def edit_monthly_subscribers(request,id):

    monthly_member = get_object_or_404(MonthlyPackage, id=id)

    if request.method == 'POST':
        form = MonthlyPackageForm(request.POST,request.FILES , instance = monthly_member)
        if form.is_valid():
            form.save()
            messages.success(request, 'student updated successfully')
            return redirect('index')
        else:
            messages.error(request, 'student not updated')

    else:
        form = MonthlyPackageForm(instance= monthly_member)
    return render(request, 'edit_monthly_subscribers.html', {"form": form,'monthly_member':monthly_member})

def delete_monthly_subscribers(request,id):
    monthly_member = get_object_or_404(MonthlyPackage, id=id)

    try:
        monthly_member.delete()
        messages.success(request, 'student deleted successfully')
    except Exception as e:
        messages.error(request, 'message not deleted')
    return redirect('members')
# def half_members(request):
#     half_data = HalfPackage.objects.all()
#     return render(request, 'members.html',{"half_data":half_data})

#  update in members.html

def edit_half_subscribers(request,id):

    six_months = get_object_or_404(HalfPackage, id=id)

    if request.method == 'POST':
        form = HalfPackageForm(request.POST,request.FILES, instance = six_months)
        if form.is_valid():
            form.save()
            messages.success(request, 'student updated successfully')
            return redirect('members')
        else:
            messages.error(request, 'student not updated')
    else:
        form =  HalfPackageForm(instance= six_months)
    return render(request, 'edit_half_subscribers.html', {"form": form,'six_months': six_months})

def delete_half_subscribers(request,id):

    six_months = get_object_or_404(HalfPackage, id=id)

    try:
        six_months.delete()
        messages.success(request, 'student deleted successfully')
    except Exception as e:
        messages.error(request, 'message not deleted')
    return redirect('members')



def edit_yearly_subscribers(request,id):

    yearly = get_object_or_404(YearlyPackage, id=id)

    if request.method == 'POST':
        form = YearlyPackageForm(request.POST, instance = yearly)
        if form.is_valid():
            form.save()
            messages.success(request, 'student updated successfully')
            return redirect('members')
        else:
            messages.error(request, 'student not updated')
    else:
        form = YearlyPackageForm(instance= yearly)
    return render(request, 'edit_yearly_subscribers.html', {"form": form,'yearly': yearly})

def delete_yearly_subscribers(request,id):
    yearly = get_object_or_404(YearlyPackage, id=id)
    try:
        yearly.delete()
        messages.success(request, 'student deleted successfully')
    except Exception as e:
        messages.error(request, 'message not deleted')
    return redirect('members')



def admin_dashboard(request):
    total_members = Student.objects.count()
    monthly_members = MonthlyPackage.objects.count()
    six_month_members = HalfPackage.objects.count()
    yearly_members = YearlyPackage.objects.count()
    return render(request, 'admin_dashboard.html', {
        'total_members': total_members,
        'monthly_members': monthly_members,
        'six_month_members': six_month_members,
        'yearly_members': yearly_members,
    })

# serializers view
@api_view(['GET', 'POST'])
def studentsapi(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return JsonResponse(serializer.data , safe=False)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # 201 new record has been fetched
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def mpesaapi(request):
    client = MpesaClient()
    phone_number = '0748400973'
    amount = 1
    account_reference = 'ronoh'
    transaction_desc = 'payment for web dev'
    callback_url = 'https://darajambili.herokuapp.com/express-payment';
    response = client.stk_push(phone_number,amount,account_reference,transaction_desc,callback_url)
    return HttpResponse(response)