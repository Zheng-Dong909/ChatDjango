
from django.shortcuts import render, redirect

def index(request):
    return render(request, "index.html")


# def login(request):
#     return render(request, "login.html")


def room(request, room_name):
    return render(request, "chat.html", {"room_name": room_name})



