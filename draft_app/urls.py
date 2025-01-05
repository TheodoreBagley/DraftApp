from django.urls import path
from . import views

urlpatterns = [
    path("", views.start_screen, name="start_screen"),
    path("draft", views.draft_screen, name="draft_screen"),
    path("learn", views.learn_screen, name="learn_screen"),
    path("learn/ban", views.ban_screen, name="ban_screen"),
]