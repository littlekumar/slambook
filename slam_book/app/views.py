from django.core.mail import send_mail
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.generic import TemplateView
from .models import Admin_Login1,User_Login1


# Create your views here.
def showindex(request):
    return render(request,"home.html")






class ShowAdmin(TemplateView):


    template_name1="Admin_registration.html"



class Main(TemplateView):
    template_name = "home.html"


class User_Registration(TemplateView):
    template_name = "User_registration.html"


class Admin_Login(TemplateView):

    template_name = "Admin_Login.html"




def admin_validation(request):

    email = request.POST.get("email1")
    password = request.POST.get("password1")

    if Admin_Login1.objects.filter(email=email) and Admin_Login1.objects.filter(password=password):
            mess = "Admin Login Successfully......"
            return render(request, 'Admin_Login.html', {"message": mess})
    else:
            mess = "Invalid User name and Password"
            return render(request, 'Admin_registration.html', {"data": mess})



    #
    # if Admin_Login(email1=email,password1=password):
    #     return render(request,"admin_login.html")
    # else:
    #     message="wrong email or password"
    #     return render(request,"Admin_Login.html",{"message":message})


def store_user(request):

    first_name = request.POST.get("first name")
    last_name = request.POST.get("last name")
    name = request.POST.get("name")

    email = request.POST.get("email")
    password = request.POST.get("password")
    phone_number = request.POST.get("phone")

    User_Login1(first_name=first_name,last_name=last_name ,name=name,email=email,password=password,phone_number=phone_number).save()

    return render(request,"user_Login.html",{"message":"User Created Succesfully"})


def user_login(request):
    email = request.POST.get("Email")
    password = request.POST.get("Password")

    if User_Login1.objects.filter(email=email) and User_Login1.objects.filter(password=password):

        mess = "Welcome"
        return render(request, 'user.html', {"message": mess,})
    else:
        mess = "Invalid User name and Password"

        return render(request, 'User_login.html', {"data": mess})

