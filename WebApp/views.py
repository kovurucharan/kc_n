from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout,get_user_model
# Create your views here.
from WebApp.models import StudentApplication,StaffRegistration,SRegistration
from django.contrib.auth.decorators import login_required

def Home(request):
    return render (request,'MyApp/home.html')

def StdApplication(request):
    return render(request, 'MyApp/stdapplication.html')

def SApliSave(request):
    if request.method == 'POST':
        StudentApplication.objects.create(student_name = request.POST['student_name'],
                                          student_email = request.POST['student_email'],
                                          ssc_marks = request.POST['ssc_marks'],
                                          inter_marks = request.POST['inter_marks'])
        return HttpResponseRedirect('/sreg/')


def Sregister(request):
    return render(request,'MyApp/sregister.html/')

@login_required(login_url="/slogin/")
def StdReg(request):
    std = StudentApplication.objects.get(student_email=request.POST["email"],)
    if request.method == 'POST' and std.is_approved == True:
        user = User.objects.create_user(
            username=request.POST['username'],
            email=request.POST["email"],
            password=request.POST['password'],
            is_staff = 'False'
        )
        user.set_password('password')
        SRegistration.objects.create(student=user,
                               student_app = std,
                               mobile=request.POST['mobile'],
                               profile_pic=request.FILES['profile_pic'],
                               department=request.POST['department'],
                               gender=request.POST['gender'],
                               father_name=request.POST['father_name'])
        return HttpResponseRedirect('/')
    else:
        return HttpResponse("Not Valid user")

def Login(request):
    return render(request,'MyApp/login.html')


def Stddetails(request):
    return  render(request,'MyApp/stddetails.html')

@login_required(login_url="/slogin/")
def Stdlist(request):
    user = User.objects.filter(is_staff='False')
    return render(request, 'MyApp/stdlist.html', {"obj": user})


def check(request):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(email=request.POST['email'])
    except UserModel.DoesNotExist:
        return HttpResponse('Student credentials are not correct')
    else:
        if user.check_password(request.POST['password']):
            login(request, user)
            student = SRegistration.objects.get(student=user)
            appl_data = StudentApplication.objects.get(student_email=request.POST['email'])
            data = {
                'Name' :student.student.username,
                "Email":student.student.email,
                "Department" : student.department,
                "Data" : student.profile_pic,
                "sscmarks" : appl_data.ssc_marks,
                "intermarks" : appl_data.inter_marks
            }
            return render(request,'MyApp/stddetails.html',{'data' : data})
    return HttpResponse('Student credentials are not correct')


def stdlogout(request):
    logout(request)
    return HttpResponseRedirect('/slogin/')


def Staffreg(request):
    return render(request,'MyApp/staffreg.html')

def staff_save(request):
    if request.method == 'POST':
        user = User.objects.create_user(
            username=request.POST['username'],
            email=request.POST["email"],
            password=request.POST['password'],
            is_staff='True'
        )
        user.set_password('password')
        StaffRegistration.objects.create(staff=user,
                             staff_mob=request.POST['staff_mob'],
                             staff_dept=request.POST['staff_dept'],
                             staff_pic=request.FILES['staff_pic'],
                             qualification=request.POST['qualification'],
                             experience=request.POST['experience'],
                             staff_gender=request.POST['staff_gender']
        )

    return HttpResponseRedirect('/stflogin/')

def Stflogin(request):
    return render(request,'MyApp/stafflogin.html')

@login_required(login_url="/stflogin/")
def Stflist(request):
    user = User.objects.filter(is_staff="True")
    return render(request, 'MyApp/stafflist.html', {'user' : user})

@login_required(login_url="/stflogin/")
def Staffcheck(request):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(email=request.POST['email'])
    except UserModel.DoesNotExist:
        return HttpResponse('Staff credentials are not correct')
    else:
        if user.check_password(request.POST['password']):
            login(request, user)
            staff =StaffRegistration.objects.get(staff=user)
            staff_data = {
                "name" : staff.staff.username,
                "email" : staff.staff.email,
                "department" : staff.staff_dept,
                "qualification" : staff.qualification,
                "experience" : staff.experience,
                "mobile" : staff.staff_mob
            }
            return render(request,'MyApp/stffdetails.html',{"data" : staff_data})
    return HttpResponse('Staff credentials are  not correct')



def stafflogout(request):
    logout(request)
    return HttpResponseRedirect('/stflogin/')

def Departments(request):
    return render(request, 'MyApp/departments.html')

def stdeptlist(request):
    dplist=SRegistration.objects.filter(department=request.POST['department'])
    return render(request,'MyApp/deptlist.html',{'dp':dplist})























