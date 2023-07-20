from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from uww.views import HomePageView, TournamentView,TournamentAddView, TournamentViewSet, AboutTournamentView, TournamentDeleteView


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("tournament_add/", TournamentAddView.as_view(), name="tournament_add"),
    path("deltournament/", TournamentDeleteView.as_view(), name="deltournament"),
    path("tournament/<int:pk>/", AboutTournamentView.as_view(), name="tournament"),
]
router = DefaultRouter()
router.register("api/v1/tournaments", TournamentViewSet, basename="tournaments")
urlpatterns += router.urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)