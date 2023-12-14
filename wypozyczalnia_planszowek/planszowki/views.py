from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Gatunek, Gra, Wypozyczajacy, Wypozyczenie, Komentarz, Account
from .serializers import GatunekSerializer, GraSerializer, WypozyczajacySerializer, WypozyczenieSerializer, \
    KomentarzSerializer, AccountSerializer
from django.contrib.auth import login
from django.contrib.auth.models import Group
from django.views.generic import FormView
from .forms import UserForm
from rest_framework.authtoken.models import Token


class BearerTokenAuthentication(TokenAuthentication):
    keyword = u"Bearer"


def index(request):
    return HttpResponse("Jesteś na stronie z planszówkami")


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def lista_gier(request):
    if request.method == 'GET':
        gry = Gra.objects.all()
        serializer = GraSerializer(gry, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def lista_gier_zawiera(request, search_string):
    if request.method == 'GET':
        gry = Gra.objects.filter(tytul__icontains=search_string)
        serializer = GraSerializer(gry, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([BearerTokenAuthentication])
@permission_classes([IsAuthenticated])
def gra_detail(request, pk):
    try:
        gra = Gra.objects.get(pk=pk)
    except Gra.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GraSerializer(gra)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = GraSerializer(gra, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        gra.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def gra_add(request):
    if request.method == 'POST':
        serializer = GraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def lista_gatunkow(request):
    if request.method == 'GET':
        gatunki = Gatunek.objects.all()
        serializer = GatunekSerializer(gatunki, many=True)
        return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def gatunek_add(request):
    if request.method == 'POST':
        serializer = GatunekSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([BearerTokenAuthentication])
@permission_classes([IsAuthenticated])
def gatunek_detail(request, pk):
    try:
        gatunek = Gatunek.objects.get(pk=pk)
    except Gra.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GatunekSerializer(gatunek)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = GatunekSerializer(gatunek, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        gatunek.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def gry_gatunku(request, pk):
    if request.method == 'GET':
        gry = Gra.objects.filter(gatunek=pk)
        serializer = GraSerializer(gry, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def lista_uzytkownikow(request):
    if request.method == 'GET':
        osoby = Wypozyczajacy.objects.all()
        serializer = WypozyczajacySerializer(osoby, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([BearerTokenAuthentication])
@permission_classes([IsAuthenticated])
def wypozyczajacy_detail(request, pk):
    try:
        osoba = Wypozyczajacy.objects.get(pk=pk)
    except Wypozyczajacy.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WypozyczajacySerializer(osoba)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = WypozyczajacySerializer(osoba, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        osoba.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def wypozyczajacy_add(request):
    if request.method == 'POST':
        serializer = WypozyczajacySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def lista_wypozyczen_uzytkownika(request, pk):
    if request.method == 'GET':
        wypozyczenie = Wypozyczenie.objects.filter(wypozyczajacy=pk)
        serializer = WypozyczenieSerializer(wypozyczenie, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def wypozyczenia_miesiac(request, pk):
    if request.method == 'GET':
        wypozyczenie = Wypozyczenie.objects.all()
        miesiac = []
        for i in wypozyczenie:
            if i.data_wypozyczenia.month == pk:
                miesiac.append(i)
        serializer = WypozyczenieSerializer(miesiac, many=True)
        return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def wypozyczenie_add(request):
    if request.method == 'POST':
        serializer = WypozyczenieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([BearerTokenAuthentication])
@permission_classes([IsAuthenticated])
def wypozyczenie_detail(request, pk):
    try:
        wypozyczenie = Wypozyczenie.objects.get(pk=pk)
    except Wypozyczenie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WypozyczenieSerializer(wypozyczenie)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = WypozyczenieSerializer(wypozyczenie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        wypozyczenie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def lista_komentarzy_gry(request, pk):
    if request.method == 'GET':
        komentarz = Komentarz.objects.filter(gra=pk)
        serializer = KomentarzSerializer(komentarz, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def komentarze_ocena(request, pk):
    if request.method == 'GET':
        komentarz = Komentarz.objects.filter(ocena=pk)
        serializer = KomentarzSerializer(komentarz, many=True)
        return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def komentarz_add(request):
    if request.method == 'POST':
        serializer = KomentarzSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([BearerTokenAuthentication])
@permission_classes([IsAuthenticated])
def komentarz_detail(request, pk):
    try:
        komentarz = Komentarz.objects.get(pk=pk)
    except Komentarz.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = KomentarzSerializer(komentarz)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = KomentarzSerializer(komentarz, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        komentarz.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserRegistrationView(FormView):
    template_name = 'register.html'
    success_url = '/planszowki/gry/'
    form_class = UserForm

    def form_valid(self, form):
        user = form.save()
        Account.objects.create(user=user)
        Token.objects.get_or_create(user=user)
        user.groups.add(Group.objects.get(name='userzy'))
        login(self.request, user)
        return super().form_valid(form)
