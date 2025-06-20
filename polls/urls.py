from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("index", views.index, name="index"),
    path("details", views.details, name="details"),
    path("result", views.result, name="result"),
    path("vote", views.vote, name="vote")
]