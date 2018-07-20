from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from schedule.models import Schedule
from schedule.serializers import ScheduleListSerializer
import pdb
from schedule.oauth2token import get_token

class ScheduleApiView(APIView):
    def get(self, request, format=None):
        code = request.META['HTTP_CODE']
        get_token(code)
        schedules = Schedule.objects.all()
        serializer = ScheduleListSerializer(schedules, many=True)

        return Response({'data':serializer.data}, status=200)
