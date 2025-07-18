from django.contrib import admin
from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.details, name="details"),
    path("<int:question_id>/result/", views.result, name="result"),
    path("<int:question_id>/vote/", views.vote, name="vote")
]