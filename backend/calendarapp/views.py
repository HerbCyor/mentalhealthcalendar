from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.status import HTTP_200_OK
from .models import Calendar, Day
from .serializers import DaySerializer
from django.shortcuts import get_object_or_404

class DayAPIView(APIView):
    def get(self,request,calendar_id):
        result = Day.objects.filter(calendar__id=calendar_id)
        serializer = DaySerializer(result,many=True)
        return Response(serializer.data,status=HTTP_200_OK)


class CreateDayAPIView(APIView):
    def post(self,request):
    
        calendar = get_object_or_404(Calendar, id=request.data.get('calendar'))
        date = request.data.get('date')
        day = Day.objects.filter(calendar=calendar,date=date).first()
        if day:
            serializer = DaySerializer(instance=day, data=request.data)
        else:
            serializer = DaySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

