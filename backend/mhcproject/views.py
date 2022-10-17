from django.shortcuts import render,get_object_or_404,redirect
from calendarapp.models import Calendar,Day
from django.contrib.auth import authenticate,login, logout
from .forms import NewUserForm
from django.contrib import messages
from decouple import config

def index(request):
    return render(request, 'index.html')

def login_view(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request,user)
            return redirect('calendar')

    return redirect('index')

def logout_view(request):
    logout(request)
    return redirect ('index')

def register_user(request):
    message = ""
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            message = messages.success(request, "Registration successful." )
            return redirect('calendar')
        message = messages.error(request, "Unsuccessful registration. Invalid information." )
    
    form = NewUserForm()
    context = {
        'register_form':form,
        'messages':message,
    }
    return render(request,"register.html", context)

def calendar(request):
    
    if not request.user.is_authenticated:
        return redirect('login-view')

    calendar = get_object_or_404(Calendar, user=request.user)
    days = Day.objects.filter(calendar=calendar)
    statistics_api_url = config('STATISTICS_API_BASE_URL') + "/daystats/"
    context = {
        'calendar' : calendar,
        'days' : days,
        'statistics_api_url':statistics_api_url
    }
    
    return render(request,"calendar.html",context)

def createDay(request):

    if request.method == 'POST':
        calendar = get_object_or_404(Calendar, id=request.POST.get('calendar'))
        date = request.POST.get('date')
        day = Day.objects.filter(calendar=calendar,date=date).first()
        if day:
            day.mood_score = request.POST.get('mood_score')
            day.comments = request.POST.get('comments')
            day.save()
        else:
            new_day = Day(
                calendar = calendar,
                date=date,
                mood_score = request.POST.get('mood_score'),
                comments = request.POST.get('comments')
            )
            new_day.save()
        
    return redirect('calendar')