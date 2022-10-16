from django.contrib import admin
from .models import Calendar, Day

class CalendarAdmin(admin.ModelAdmin):
    list_display= ['name',]

class DayAdmin(admin.ModelAdmin):
    list_display = ['calendar','date','mood_score','comments']

admin.site.register(Calendar,CalendarAdmin)
admin.site.register(Day,DayAdmin)
