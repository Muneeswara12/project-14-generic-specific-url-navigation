from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def gt(request):
    return render(request,'gt.html')