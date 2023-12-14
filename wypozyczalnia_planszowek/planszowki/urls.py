from django.urls import path
from . import views
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('', views.index, name='index'),
    path('gry/', views.lista_gier),
    path('gry/<str:search_string>/', views.lista_gier_zawiera),
    path('gry/info/<int:pk>/', views.gra_detail),
    path('gry_add/', views.gra_add),
    path('gatunki/', views.lista_gatunkow),
    path('gatunki_add/', views.gatunek_add),
    path('gatunki/<int:pk>/', views.gatunek_detail),
    path('gatunki/<int:pk>/gry/', views.gry_gatunku),
    path('gracze/', views.lista_uzytkownikow),
    path('gracze_add/', views.wypozyczajacy_add),
    path('gracze/<int:pk>/', views.wypozyczajacy_detail),
    path('gracze/<int:pk>/wypozyczenia/', views.lista_wypozyczen_uzytkownika),
    path('wypozyczenia_add/', views.wypozyczenie_add),
    path('wypozyczenia/<int:pk>/', views.wypozyczenie_detail),
    path('wypozyczenia/miesiaca/<int:pk>/', views.wypozyczenia_miesiac),
    path('gry/<int:pk>/komentarze/', views.lista_komentarzy_gry),
    path('komentarze/ocena/<int:pk>/', views.komentarze_ocena),
    path('komentarze_add/', views.komentarz_add),
    path('komentarze/<int:pk>/', views.komentarz_detail),
    path('api-token-auth/', obtain_auth_token),
    path('rejestracja/', views.UserRegistrationView.as_view()),
]
