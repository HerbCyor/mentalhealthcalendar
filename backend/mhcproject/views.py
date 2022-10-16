from django.shortcuts import render,get_object_or_404,redirect
from calendarapp.models import Calendar,Day

def index(request):
    calendar = Calendar.objects.all()[0]
    days = Day.objects.filter(calendar=calendar)
    context = {
        'calendar' : calendar,
        'days' : days[1].__dict__
    }
    return render(request,"index.html",context)

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
        
    return redirect('index')