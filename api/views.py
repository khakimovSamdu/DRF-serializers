from django.shortcuts import render
from rest_framework.views import View

from .models import Talaba
from .serializers import TalabaSerilazers

from django.http import HttpResponse, HttpRequest, JsonResponse
# Create your views here.
class TalabaViews(View):
    def get(self,request: HttpRequest):
        talaba = Talaba.objects.all()
        ruyxat = []
        for item in talaba:
            serializers = TalabaSerilazers(item)
            data = serializers.data
            ruyxat.append(data)
        return JsonResponse(data=ruyxat, safe=False)
    