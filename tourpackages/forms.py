# forms.py
from django import forms

class IntegerDateForm(forms.Form):
    integer_value = forms.IntegerField()
    date_value = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

class carrentdate(forms.Form):
    location = forms.CharField()
    from_date_value = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    to_date_value = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


# your_app/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)


# class CustomAuthenticationForm(AuthenticationForm):
#     username = forms.EmailField(widget=forms.TextInput(attrs={'autofocus': True}))


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Enter your email address'



# forms.py
from django import forms

class PieChartForm(forms.Form):
    y_values = forms.CharField(label='Y Values', help_text='Enter comma-separated values')
    labels = forms.CharField(label='Labels', help_text='Enter comma-separated labels')
