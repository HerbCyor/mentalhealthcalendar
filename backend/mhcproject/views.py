from django.shortcuts import render,get_object_or_404,redirect
from calendarapp.models import Calendar,Day
from django.contrib.auth import authenticate,login

def index(request):
    return render(request, 'index.html')

def login_user(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request,user)
            return redirect('calendar-view')
            
    return redirect('index')

def calendar(request):
    
    if not request.user.is_authenticated:
        return redirect('login-user')

    calendar = get_object_or_404(Calendar, user=request.user)
    days = Day.objects.filter(calendar=calendar)
    context = {
        'calendar' : calendar,
        'days' : days
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