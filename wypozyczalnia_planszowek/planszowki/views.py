from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Gatunek, Gra, Wypozyczajacy, Wypozyczenie, Komentarz
from .serializers import GatunekSerializer, GraSerializer, WypozyczajacySerializer, WypozyczenieSerializer, KomentarzSerializer


def index(request):
    return HttpResponse("Jesteś na stronie z planszówkami")


@api_view(['GET'])
def lista_gier(request):
    if request.method == 'GET':
        gry = Gra.objects.all()
        serializer = GraSerializer(gry, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def lista_gier_zawiera(request, search_string):
    if request.method == 'GET':
        gry = Gra.objects.filter(tytul__icontains=search_string)
        serializer = GraSerializer(gry, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
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
def gra_add(request):
    if request.method == 'POST':
        serializer = GraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def lista_gatunkow(request):
    if request.method == 'GET':
        gatunki = Gatunek.objects.all()
        serializer = GatunekSerializer(gatunki, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def gatunek_add(request):
    if request.method == 'POST':
        serializer = GatunekSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
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
def gry_gatunku(request, pk):
    if request.method == 'GET':
        gry = Gra.objects.filter(gatunek=pk)
        serializer = GraSerializer(gry, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def lista_uzytkownikow(request):
    if request.method == 'GET':
        osoby = Wypozyczajacy.objects.all()
        serializer = WypozyczajacySerializer(osoby, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
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
def wypozyczajacy_add(request):
    if request.method == 'POST':
        serializer = WypozyczajacySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def lista_wypozyczen_uzytkownika(request, pk):
    if request.method == 'GET':
        wypozyczenie = Wypozyczenie.objects.filter(wypozyczajacy=pk)
        serializer = WypozyczenieSerializer(wypozyczenie, many=True)
        return Response(serializer.data)


@api_view(['GET'])
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
def wypozyczenie_add(request):
    if request.method == 'POST':
        serializer = WypozyczenieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
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
def lista_komentarzy_gry(request, pk):
    if request.method == 'GET':
        komentarz = Komentarz.objects.filter(gra=pk)
        serializer = KomentarzSerializer(komentarz, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def komentarze_ocena(request, pk):
    if request.method == 'GET':
        komentarz = Komentarz.objects.filter(ocena=pk)
        serializer = KomentarzSerializer(komentarz, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def komentarz_add(request):
    if request.method == 'POST':
        serializer = KomentarzSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
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
