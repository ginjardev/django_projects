from django.shortcuts import render

# Create your views here.


def create_cohort(request):
    return render(request, 'create_cohort.html')


def home(request):
    return render(request, 'home_page.html')


def create_native(request):
    return render(request, 'create_native.html')


def display_natives(request):
    return render(request, 'display_natives.html')

