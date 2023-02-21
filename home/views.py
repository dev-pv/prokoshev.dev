from django.shortcuts import render
from home import models

def preload(request):
    return render(request, "preload.html")
def home(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        feedback = request.POST['feedback']
        ins = models.Contact(name=name, email=email, feedback=feedback)
        ins.save()
        print("data sent to db")
    return render(request, "home.html")