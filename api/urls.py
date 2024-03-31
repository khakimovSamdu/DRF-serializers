from django.urls import path
from .views import TalabaViews 
urlpatterns = [
    path('get/', TalabaViews.as_view()),
    path('get/id/<int:id>/', TalabaViews.as_view()),
    path('get/first_name/<first_name>/', TalabaViews.as_view()),
    path('get/last_name/<last_name>/', TalabaViews.as_view()),
    path('get/age/<int:age>/', TalabaViews.as_view()),
    path('get/country/<country>/', TalabaViews.as_view()),
    path('post/', TalabaViews.as_view()),
    path('delete/<int:id>/', TalabaViews.as_view()),
        
]