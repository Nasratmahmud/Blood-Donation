from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Register

# Create your views here.

# dashboard view
def dashboard_view(request):
    item = Register.objects.all()
    context = {
        'data': item
    }
    return render(request, 'html/dashboard.html', context)

# home view
def home_view(request):
    title = 'Blood Donation'
    subtitle = 'Donate Blood, Save Life'
    desc = '''
        A blood donation occurs when a person voluntarily has blood drawn and used for transfusions and/or made into biopharmaceutical medications by a process called fractionation.
        Donation may be of whole blood, or of specific components directly.
        Blood banks often participate in the collection process as well as the procedures that follow it.
    '''
    context = {
        'title': title,
        'subtitle': subtitle,
        'desc': desc
    }
    return render(request, 'html/home.html', context)

# login view
def login_view(request):
    return render(request, 'html/login.html')

# register view
def register_view(request):
    if request.method == 'POST':
        vfullname = request.POST.get('fullname')
        vage = request.POST.get('age')
        if request.POST.get('gender'):
            vgender = request.POST.get('gender')
        if request.POST.get('bloodGroup'):
            vbloodgroup = request.POST.get('bloodGroup')
        vcontact = request.POST.get('contact')
        mydata = Register(fullname=vfullname, age=vage, gender=vgender, bloodgroup=vbloodgroup, contact=vcontact)
        mydata.save()
    return render(request, 'html/register.html')
