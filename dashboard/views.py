from django.shortcuts import render

# Create your views here.


def home(request):
    context = {}
    template = 'dashboard/index.html'
    return render(request, template, context)


def about(request):
    context = {}
    template = 'dashboard/about.html'
    return render(request, template, context)


def signup(request):
    context = {}
    template = 'dashboard/signup.html'
    return render(request, template, context)
