from django.http import HttpResponse
from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.
def homepage(request):
    user_email = request.session.get('user_email')
    user = Register.objects.filter(email=user_email).first()
    return render(request, 'Homepage.html', {'user': user})
    # return render(request, 'Homepage.html')

def flights(request):
    return render(request, 'Flights.html')
def travelpackages(request):
    return render(request, 'Travelpackages.html')
def myregisterpage(request):
    return render(request, "myregisterpage.html")

def login1(request):
    return render(request, "Login1.html")

def rentcar(request):
    return render(request, "Rentcar.html")

def renthatchback(request):
    return render(request, "renthatchback.html")

def alllink(request):
    return render(request, "Alllink.html")

import datetime, time, calendar

def date1(request):
    datetime_object = datetime.datetime.now()
    s2 = calendar.month(2023, 4)
    s1 = calendar.isleap(2005)

    context = {
        'datetime_object': datetime_object,
        's2': s2,
        's1': s1,
    }
    return render(request, "Datetime123.html", context)

def randomotp(request):
    return render(request, "Randomotp.html")

import random, string
def randomotp1(request):
    if request.method == 'POST':
        input1 = request.POST['input1']
        input2 = int(input1)
        result_str = ''.join(random.sample(string.digits, input2))
        print(result_str)
        context = {'result_str': result_str}
    return render(request, "Randomotp.html", context)

def getdate1(request):
    return render(request,'get_date.html')

def getdate2(request):
    return render(request,'result.html')

from django.shortcuts import render
def get_date(request):
    if request.method == 'POST':
        form = IntegerDateForm(request.POST)
        if form.is_valid():
            integer_value = form.cleaned_data['integer_value']
            date_value = form.cleaned_data['date_value']
            updated_date = date_value + datetime.timedelta(days=integer_value)

            return render(request, 'get_date.html', {'updated_date': updated_date})
        else:
            form = IntegerDateForm()
        return render(request, 'get_date.html', {'form': form})

def print1(request):
    return render(request, 'print_to_console.html')
def print_to_console(request):
    if request.method == "POST":
        user_input = request.POST['user_input']
        print(f'User input: {user_input}')
    # return HttpResponse('Form submitted successfully')
    a1= {'user_input':user_input}
    return render(request,'print_to_console.html',a1)

def my_view(request):
    # Your view logic here
    show_alert = True  # Set this based on your condition
    return render(request, 'my_template.html', {'show_alert': show_alert})


from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm  # Import your custom form
'''
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home1')  # Replace 'home' with the name of your home view or URL
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


from django.contrib.auth import login, authenticate
from django.contrib.auth import login as auth_login  # Renaming the login function
from django.shortcuts import render, redirect
from .forms import LoginForm  # Import your LoginForm from forms.py
# your_app/views.py
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomAuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=raw_password)

            if user is not None:
                login(request, user)
                return redirect('home1')  # Replace 'home' with the name of your home view or URL
            else:
                messages.error(request, 'Invalid email or password.')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})
'''

from django.contrib.auth import login as auth_login, logout as auth_logout
def user_logout(request):
    auth_logout(request)
    return redirect('home1')

def register2(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if the email already exists
        if Register.objects.filter(email=email).exists():
            return HttpResponse("Email already registered. Choose a different email.")

        # Create a new Register instance and save it
        Register.objects.create(name=name, email=email, password=password)

        return redirect('home1')  # Replace 'home1' with the name of your home view or URL

    return render(request, 'register.html')


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view1(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = Register.objects.filter(email=email, password=password).first()

        if user is not None:
            # Log in the user
            request.session['user_email'] = user.email
            messages.success(request, 'Login successful.')
            return redirect('home1')  # Replace 'home1' with the name of your home view or URL
        else:
            messages.error(request, 'Invalid email or password.')
            return redirect('popup_view')

def home_view(request):
    # Retrieve the user's name from the session
    user_email = request.session.get('user_email')
    user = Register.objects.filter(email=user_email).first()

    return render(request, 'home.html', {'user': user})


import matplotlib.pyplot as plt
import numpy as np
def pie_chart(request):
    if request.method == 'POST':
        form = PieChartForm(request.POST)
        if form.is_valid():
            # Process user input
            y_values = [int(val) for val in form.cleaned_data['y_values'].split(',')]
            labels = [label.strip() for label in form.cleaned_data['labels'].split(',')]

            # Create pie chart
            plt.pie(y_values, labels=labels, startangle=90)
            plt.savefig('static/images/pie_chart.png')  # Save the chart image
            img1={'chart_image': '/static/images/pie_chart.png'}
            return render(request, 'chart_form.html', img1)
    else:
        form = PieChartForm()
    return render(request, 'chart_form.html', {'form': form})
def contactform(request):
    return render(request, 'Contact.html')

from django.core.mail import send_mail
def contactmail(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        comment = request.POST['comment']
        tosend= comment + '-------------------- This is just the copy of comment what you have posted in MMS System'
        data = contactus(firstname=firstname, lastname=lastname, email=email, comments=comment)
        data.save()
        send_mail(
            'Thank You for Contacting Deepaks Travel Tourism and Management  System',
            tosend,
            'justw9090@gmail.com',
            [email],
            fail_silently=False,
        )
        return HttpResponse("<h1><center>Mail Sent</center></h1>")
        # return render(request, 'Homepage.html')
    else:
        HttpResponse("<h1>error</h1>")

from datetime import timedelta

'''
def rentcarlogic(request):
    if request.method == 'POST':
        location1 = request.POST.get('location1')
        from_date_value = request.POST['from_date_value']
        to_date_value = request.POST['to_date_value']

        # Create a new RentCar instance
        RentCar.objects.create(location1=location1, from_date_value=from_date_value, to_date_value=to_date_value)

    # Calculate the total date difference
    try:
        rentcar_instances = RentCar.objects.all()

        total_date_difference = 0

        for rentcar_instance in rentcar_instances:
            if rentcar_instance.from_date_value and rentcar_instance.to_date_value:
                # Adding 1 to consider the same date as a difference of 1 day
                date_difference = (rentcar_instance.to_date_value - rentcar_instance.from_date_value).days + 1
                total_date_difference += date_difference

        total_date_difference_message = f"The total date difference for all RentCar instances is {total_date_difference} days."

    except RentCar.DoesNotExist:
        total_date_difference_message = "No RentCar instances found."

    return render(request, 'renthatchback.html', {'total_date_difference_message': total_date_difference_message})

'''
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta

from django.shortcuts import render, redirect
from datetime import datetime

def rentcarlogic(request):
    global Total_Fare
    total_date_difference_message = ""
    # Total_Fare=10 # Define Total_Fare before the conditional block

    if request.method == 'POST':
        location1 = request.POST.get('location1')
        from_date_value = request.POST.get('from_date_value')
        to_date_value = request.POST.get('to_date_value')
        # Convert the date strings to datetime objects
        button_type = request.POST.get('button_type')
        from_date = datetime.strptime(from_date_value, "%Y-%m-%d")
        to_date = datetime.strptime(to_date_value, "%Y-%m-%d")

        # Calculate the date difference
        date_difference = (to_date - from_date).days + 1
        print(date_difference)
        total_date_difference_message = f"The date difference is {date_difference} days."
        Base_Price = 2000 * date_difference
        Driver_Allowance = 2000
        GST = (Base_Price * 5) / 100
        Total_Fare = Base_Price + Driver_Allowance + GST
        data = {'Base_Price': Base_Price, 'Driver_Allowance': Driver_Allowance, 'GST': GST, 'Total_Fare': Total_Fare}
        print(Total_Fare)
        request.session['Total_Fare'] = Total_Fare
        if button_type == 'rent_now':
            # from_date = datetime.strptime(from_date_value, "%Y-%m-%d")
            # to_date = datetime.strptime(to_date_value, "%Y-%m-%d")
            #
            # # Calculate the date difference
            # date_difference = (to_date - from_date).days + 1
            # print(date_difference)
            # total_date_difference_message = f"The date difference is {date_difference} days."
            # Base_Price = 2000 * date_difference
            # Driver_Allowance = 2000
            # GST = (Base_Price * 5) / 100
            # Total_Fare = Base_Price + Driver_Allowance + GST
            # data = {'Base_Price': Base_Price, 'Driver_Allowance': Driver_Allowance, 'GST': GST, 'Total_Fare': Total_Fare}
            # print(Total_Fare)
            # request.session['Total_Fare'] = Total_Fare
            # Total_Fare = Total_Fare1
            # Include calculated values in the URL as parameters
            return render(request, 'renthatchback.html', data)
        elif button_type == 'proceed_to_payment':
            # request.session['Total_Fare'] = Total_Fare
            # print(Total_Fare)
            return redirect('generate_qr_code')
            # return generate_qr_code(request,Total_Fare)
    # request.session['Total_Fare'] = Total_Fare
    return render(request, 'renthatchback.html')


from django.shortcuts import render
import qrcode
from PIL import Image

def generate_qr_code(request):
    Total_Fare = request.GET.get('Total_Fare', '')
    print(f"Total Fare: {Total_Fare}")
    print(Total_Fare)
    print(request.GET)
    # Replace 'your_upi_id' and 'your_amount' with the actual UPI ID and amount
    upi_id = 'vd@paytm'
    amount = Total_Fare

    # Format the payment URL with UPI ID and amount
    # payment_url = f'upi://pay?pa={upi_id}&mc=your_merchant_code&tid=your_transaction_id&tr=your_transaction_reference_id&tn=Payment&am={amount}&cu=INR&url=your_url'

    # Generate QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(upi_id+amount)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image or use it in the response
    img.save('static/images/KLU1.png')
    print('image created')

    # Add context data if needed
    context = {
        'upi_id': upi_id,
        'amount': amount,
        # 'payment_url': payment_url,
    }

    return render(request, 'generate_qr_code.html', context)

def Bookroom(request):
    return render(request, 'Bookroom.html')

import requests
def weatherpagecall(request):
    return render(request, 'weatherappinput.html')

def weatherlogic(request):
    if request.method == 'POST':
        place = request.POST['place']
        API_KEY = '98c9fe0696484df631f05ef073b66aa4'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            temperature1= round(temperature - 273.15,2)
            return render(request, 'weatherappinput.html',
                          {'city': str.upper(place), 'temperature1': temperature1, 'humidity': humidity})
        else:
            error_message = 'City not found. Please try again.'
            return render(request, 'weatherappinput.html', {'error_message': error_message})


#------------------------------------------------------------
# views.py
# from .models import CustomUser
def deepaklogin(request):
    return render(request,'deepaklogin.html')
def deepaksignup(request):
    return render(request,'deepaksignup.html')
from django.contrib.auth import get_user_model
User = get_user_model()

def deepaksignup1(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']  # New field
        pass1 = request.POST['password']
        pass2 = request.POST['password1']
        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Oops! Username already taken')
                return render(request, 'signup.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Oops! Email already taken')
                return render(request, 'signup.html')
            else:
                user = User.objects.create_user(username=username, email=email, password=pass1)
                user.save()
                messages.info(request, 'Account created successfully!!')
                return render(request, 'login.html')
        else:
            messages.info(request, 'Passwords do not match')
            return render(request, 'signup.html')
    else:
        return render(request, 'signup.html')

# views.py
from django.contrib.auth.models import User,auth
def deepaklogin1(request):
    if request.method == 'POST':
        email = request.POST['email']  # Use email instead of username
        pass1 = request.POST['password']
        user = auth.authenticate(email=email, password=pass1)
        if user is not None:
            auth.login(request, user)
            return render(request, 'index.html')
        else:
            messages.info(request, 'Invalid credentials')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')
