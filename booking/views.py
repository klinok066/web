import re

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import ReservationForm
from .models import Reservation


def index(request):
    data = {
        'title': 'Бронирование'
    }
    return render(request, 'booking/index.html', data)


def about(request):
    return render(request, 'booking/about.html')


def invalid_data(request):
    return render(request, 'booking/invalid_data.html')


def success(request):
    return render(request, 'booking/success.html')


def form(request):
    return render(request, 'booking/form.html')


regex = re.compile(
    r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
reg_phone = re.compile('(\+7|8)\D*\d{3}\D*\d{3}\D*\d{2}\D*\d{2}')


def form(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid() \
                and re.fullmatch(regex, (form.cleaned_data.get('email'))) \
                and str(form.cleaned_data.get('count')).isdigit() \
                and reg_phone.search(
            (str(form.cleaned_data.get('phone_number')))):
            form.save()
            return redirect('success')
        else:
            return redirect('invalid_data')
    form = ReservationForm()
    data = {
        'form': form,
    }
    return render(request, 'booking/form.html', data)


@login_required
def records(request):
    reservations = Reservation.objects.all()
    return render(request, 'booking/records.html', {'reservations': reservations})