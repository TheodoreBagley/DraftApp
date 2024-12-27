from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def start_screen(request):
    template = loader.get_template("draft_app/start_screen.html")

    return HttpResponse(template.render())