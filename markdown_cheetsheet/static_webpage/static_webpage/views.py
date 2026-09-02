from django.shortcuts import render

def home_handler(r):
    return render(r, "index.html")