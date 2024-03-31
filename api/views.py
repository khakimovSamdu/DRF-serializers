from django.shortcuts import render
from rest_framework.views import View
import json

from .models import Talaba
from .serializers import TalabaSerilazers

from django.http import HttpResponse, HttpRequest, JsonResponse
# Create your views here.
class TalabaViews(View):
    def get(self,request: HttpRequest, id = None, first_name = None, last_name = None, age = None, country = None):
        
        if id:
            data = Talaba.objects.get(id=id)
            serializers = TalabaSerilazers(data)
            f1 = serializers.data
            return JsonResponse(f1)
        elif first_name:
            data = Talaba.objects.filter(first_name__contains = first_name)
            ruyxat = []
            for item in data:
                serializers = TalabaSerilazers(item)
                f2 = serializers.data
                ruyxat.append(f2)
            return JsonResponse(ruyxat, safe=False)
        
        elif last_name:
            data = Talaba.objects.filter(last_name__contains = last_name)
            ruyxat = []
            for item in data:
                serializers = TalabaSerilazers(item)
                f3 = serializers.data
                ruyxat.append(f3)
            return JsonResponse(f3, safe=False)
        elif age:
            data = Talaba.objects.filter(age__ltr = age)
            ruyxat = []
            for item in data:
                serializers = TalabaSerilazers(item)
                f4 = serializers.data
                ruyxat.append(f4)
            return JsonResponse(ruyxat, safe=False)
        elif country:
            data = Talaba.objects.filter(country__contains = country)
            ruyxat = []
            for item in data:
                serializers = TalabaSerilazers(item)
                f5 = serializers.data
                ruyxat.append(f5)
            return JsonResponse(ruyxat, safe=False)
        else:
            talaba = Talaba.objects.all()
            ruyxat = []
            for item in talaba:
                serializers = TalabaSerilazers(item)
                data = serializers.data
                ruyxat.append(data)
            return JsonResponse(data=ruyxat, safe=False)
    def post(self, request: HttpRequest):
        data = request.body.decode('utf-8')
        data = json.loads(data)
        obj = Talaba.objects.create(
            first_name =  data['first_name'],
            last_name = data['last_name'],
            age = data['age'],
            country = data['country']
        )
        return JsonResponse({"post":"Talaba add accept"})
    def delete(self, request: HttpRequest, id: int):
        obj = Talaba.objects.get(id = id)
        obj.delete()
        return JsonResponse({"delete":"Status code accept"})
    
    
    
