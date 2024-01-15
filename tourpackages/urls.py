from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from .views import rentcarlogic, generate_qr_code


urlpatterns = [
    path('',views.homepage, name = 'home1'),
    path('flights/',views.flights, name = 'flights'),
    path('rentcar/', views.rentcar, name = 'rentcar'),
    path('travelpackages/', views.travelpackages, name = 'travelpackages'),
    # path('register/', views.register, name = 'register1'),
    path('login1/', views.login1, name = 'login1'),
    path('alllink/', views.alllink, name = 'alllink'),
    path('date1/', views.date1, name = 'date1'),
    path('randomotp/', views.randomotp, name = 'randomotp'),
    path('randomotp1/', views.randomotp1, name='randomotp1'),
    path('getdate/', views.get_date, name='get_date'),
    path('getdate1/', views.getdate1, name='getdate1'),
    path('getdate2/', views.getdate2, name='getdate2'),
    path('print/', views.print_to_console, name='print_to_console'),
    path('p/', views.print1, name='print1'),
    path('popup/', views.my_view, name='popup_view'),
    # path('register/', views.register, name='register'),
    # path('login2/',views.login_view,name = 'login2'),
    # path('login1/', views.login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('myregisterpage/', views.myregisterpage, name='myregisterpage'),
    path('register2/', views.register2, name = 'register2'),
    path('login_view1/', views.login_view1, name = 'login_view1'),
    path('pie_chart/', views.pie_chart, name='pie_chart'),
    path('contactform/', views.contactform, name='contactform'),
    path('contactmail/', views.contactmail, name='contactmail'),
    path('renthatchback/', views.renthatchback, name='renthatchback'),
    path('rentcarlogic/', views.rentcarlogic, name='rentcarlogic'),
    path('generate-qr-code/', generate_qr_code, name='generate_qr_code'),
    path('Bookroom/', views.Bookroom, name='Bookroom'),
    path('weatherpagecall/',views.weatherpagecall, name='weatherpagecall'),
    path('weatherlogic/', views.weatherlogic, name='weatherlogic'),
    path('deepaksignup1/', views.deepaksignup1, name='deepaksignup1'),
    path('deepaklogin1/', views.deepaklogin1, name='deepaklogin1'),
    path('deepaksignup/', views.deepaksignup, name='deepaksignup'),
    path('deepaklogin/', views.deepaklogin, name='deepaklogin'),


    ]


