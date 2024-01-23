from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm, TextInput, DateTimeInput

from .models import Reservation


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['username', 'phone_number', 'email', 'count', 'date']

        widgets = {
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ФИО'
            }),

            "phone_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Телефон'
            }),

            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Почта'
            }),

            "count": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество человек'
            }),

            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата'
            }),
        }