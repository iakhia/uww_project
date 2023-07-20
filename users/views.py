from django.db.models.query import QuerySet
from django.views.generic import ListView, View, DetailView
from django.shortcuts import render


class ProfileView(ListView):
    template_name = "profile.html"
    context_object_name = "profiles"

    def get_queryset(self):
        return 


