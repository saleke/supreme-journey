from django.shortcuts import render

def django_handler(r):
    return render(r, "django.html")

def display_handler(r):
    return render(r, "display.html")

def template_handler(r):
    return render(r, "templates.html")