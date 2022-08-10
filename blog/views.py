from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string     


def index(request):
    t = render_to_string("blog/index.html")
    
    response = JsonResponse(
        # your stuff here
    )
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"

    return response
    #return render(request, "blog/index.html", {"autoescape": False})


def test(request):
    return render(request,  "blog/test.html")
