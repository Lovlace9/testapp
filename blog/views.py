from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string     


def index(request):
    t = render_to_string("blog/index.html")
    
    return render(request, "blog/index.html", {"autoescape": False})


def test(request):
    return render(request,  "blog/test.html")