from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    university = "FPT"
    dept = "Software Engineering"
    context = {'uni':university, 'dept': dept}
    return render(request, 'home/index.html', context)