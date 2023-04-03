from django.shortcuts import render, redirect

# Create your views here.


def demo(request):
    return render(request,'index.html')