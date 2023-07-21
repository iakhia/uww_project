from typing import Any
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic import ListView, View, DetailView, DeleteView
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render, redirect
from .models import Tournament
from uww.serializers import TournamentSerializer


class HomePageView(ListView):
    template_name = "index.html"
    context_object_name = "tournaments"

    def get_queryset(self):
    
        queryset = (Tournament.objects.order_by('-pk')[ :4 ])
        return queryset
    

class AboutTournamentView(DetailView):
    model = Tournament
    template_name = 'tournament.html'
    context_object_name = 'tournaments'

    def get_queryset(self):
    
        queryset = (Tournament.objects.all())
        return queryset


class TournamentAddView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "tournament_add.html")

    def post(self, request, *args, **kwargs):
        name = request.POST.get("tournament")
        image = request.POST.get("image")
        address = request.POST.get("address")
        date = request.POST.get("date")
        tournament = Tournament(name = name, image = image, address = address, date = date)
        tournament.save()
        return redirect("home")
    

class TournamentView(ListView):
    template_name = 'tournament.html'
    context_object_name = 'tournaments'

    def get_queryset(self):
        return
    

class TournamentDeleteView(DeleteView):
    model = Tournament
    template_name = 'tournament_confirm_delete.html'
    success_url = reverse_lazy('home')

    

class TournamentViewSet(ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer

    

