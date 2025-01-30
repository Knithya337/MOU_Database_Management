from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
# Create your views here.
from .models import MOU
from .forms import CreateMOUForm
from .models import CreateMOU
from django.db.models import Count
from django.contrib import messages
MOU.objects.all()

from django.views.generic import TemplateView

from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    user = request.user  # Get the currently logged-in user
    return render(request, 'profile.html', {'user': user})


def success_url(request):
    return render(request, 'success_url.html')

def index(request):
    return render(request, 'index.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            role = form.cleaned_data.get('role')

            # Assign role based on the dropdown selection
            if role == 'admin':
                user.is_admin = True
                user.is_customer = False
                #user.is_employee = False
            elif role == 'customer':
                user.is_admin = False
                user.is_customer = True
                #user.is_employee = False
            # elif role == 'employee':
            #     user.is_admin = False
            #     user.is_customer = False
            #     user.is_employee = True

            user.save()
            msg = 'User created'
            return redirect('login_view')
        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, 'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_admin:
                    login(request, user)
                    return redirect('adminpage')
                elif user.is_customer:
                    login(request, user)
                    return redirect('customer')
                
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating form'
            
    return render(request, 'login.html', {'form': form, 'msg': msg})



def admin(request):
    return render(request,'admin.html')


def customer(request):
    return render(request,'customer.html')




# def admin_mou(request):
#     return render(request,'admin_mou.html')

def admin_progress(request):
    # Get counts of each sector and purpose
    sector_counts = MOU.objects.values('Sector').annotate(count=Count('Sector'))
    purpose_counts = MOU.objects.values('Purpose').annotate(count=Count('Purpose'))
    
    # Prepare data for charts
    sectors = [item['Sector'] for item in sector_counts]
    sector_values = [item['count'] for item in sector_counts]
    
    purposes = [item['Purpose'] for item in purpose_counts]
    purpose_values = [item['count'] for item in purpose_counts]
    
    context = {
        'sectors': sectors,
        'sector_values': sector_values,
        'purposes': purposes,
        'purpose_values': purpose_values,
    }
    
    return render(request, 'admin_progress.html', context)

def admin_report(request):
    return render(request,'admin_report.html')

def admin_activity(request):
    return render(request,'admin_activity.html')

def admin_expired(request):
    return render(request,'admin_expired.html')

def admin_renewal(request):
    return render(request,'admin_renewal.html')

def create_mou(request):
    if request.method == 'POST':
        form = CreateMOUForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Data uploaded successfully")
            return render(request, 'create_mou.html', {'form': CreateMOUForm()})  # Stay on the same page
    else:
        form = CreateMOUForm()
    
    return render(request, 'create_mou.html', {'form': form})


def admin_mou(request):
    # Get the search term from the request
    department_query = request.GET.get('department', '')
    
    # Filter the MOU records based on the search query
    if department_query:
        mou_data = MOU.objects.filter(Department__icontains=department_query)
    else:
        mou_data = MOU.objects.all()

    return render(request, 'admin_mou.html', {'mou_data': mou_data})

def cancel_url(request):
    return render(request,'create_mou.html')

def mou_list(request):
    mous = CreateMOU.objects.all()
    return render(request, 'mou_list.html', {'mous': mous})




#customer


def customer_mou(request):
    # Get the search term from the request
    department_query = request.GET.get('department', '')
    
    # Filter the MOU records based on the search query
    if department_query:
        mou_data = MOU.objects.filter(Department__icontains=department_query)
    else:
        mou_data = MOU.objects.all()

    return render(request, 'customer_mou.html', {'mou_data': mou_data})


def customer_progress(request):
    # Get counts of each sector and purpose
    sector_counts = MOU.objects.values('Sector').annotate(count=Count('Sector'))
    purpose_counts = MOU.objects.values('Purpose').annotate(count=Count('Purpose'))
    
    # Prepare data for charts
    sectors = [item['Sector'] for item in sector_counts]
    sector_values = [item['count'] for item in sector_counts]
    
    purposes = [item['Purpose'] for item in purpose_counts]
    purpose_values = [item['count'] for item in purpose_counts]
    
    context = {
        'sectors': sectors,
        'sector_values': sector_values,
        'purposes': purposes,
        'purpose_values': purpose_values,
    }
    
    return render(request, 'customer_progress.html', context)


def customer_report(request):
    mous = CreateMOU.objects.all()
    return render(request, 'customer_report.html', {'mous': mous})