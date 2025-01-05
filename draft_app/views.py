from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def start_screen(request):
    template = loader.get_template("draft_app/start_screen.html")
    return HttpResponse(template.render())

def draft_screen(request):
    template = loader.get_template("draft_app/draft_screen.html")
    return HttpResponse(template.render())

def learn_screen(request):
    template = loader.get_template("draft_app/learn_screen.html")
    return HttpResponse(template.render())

def ban_screen(request):
    template = loader.get_template("draft_app/learn_bans.html")
    return HttpResponse(template.render())