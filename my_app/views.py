from django.shortcuts import render

# Create your views here.
def about_us(request):
    return render(request,"about.html")

def agents(request):
    return render(request,"agents.html")

def contact_us(request):
    return render(request,"contact.html")

def index(request):
    return render(request,"index.html")

def properties(request):
    return render(request,"properties.html")


def services(request):
    return render(request,"services.html")

def communication(request):
    return render(request,"communication.html")




