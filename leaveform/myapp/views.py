from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Details

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method =='POST':
        username= request.POST['username']
        password= request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Credential Invalid')
            return redirect('login')
    else:
        return render(request,'login.html')

def register(request):
    if request.method =='POST':
        username = request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2 = request.POST['password2']
        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Username already Exists')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username already Used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info("Password not the same")
            return redirect('register')

    else:
        return render(request,'register.html')
    
def letter(request):
    details = Details.objects.all()
    return render(request,'letter.html',{"details":details})

def fill(request):
    if request.method =="POST":
        username=request.POST["username"]
        name=request.POST["name"]
        rno=request.POST["rno"]
        ug=request.POST["ug"]
        year=request.POST["year"]
        section=request.POST["section"]
        course=request.POST["course"]
        tot=request.POST["tot"]
        leaveletter=request.POST["leaveletter"]
        medical =request.POST["medical"]
        absent=request.POST["absent"]
        previlege=request.POST["previlege"]
        relation=request.POST["relation"]
        totdays=request.POST["totdays"]
        reason=request.POST["reason"]
        date=request.POST["date"]
        froms=request.POST["froms"]
        tos=request.POST["tos"]
        details = Details(username=username, name = name, rno = rno, ug=ug,year=year,section=section,course=course,tot=tot,leaveletter=leaveletter,medical=medical,absent=absent,previlege=previlege,relation=relation,totdays=totdays, reason=reason,date=date,froms=froms,tos=tos)
        details.save()
        return redirect('letter')

    
    return render(request,'fill.html')

def admins(request):
    details = Details.objects.all()[2:]
    return render(request,'admins.html',{"details":details})


def accept(request,id):
    new = Details.objects.all()[1]
    if (id!="2000"):
        new.name +=" "+ str(id)
        new.save()
    return render(request,'accept.html',{"new":new})


def clear(request):
    new = Details.objects.all()[1]
    new.name =''
    new.save()
    return render(request, 'clear.html')