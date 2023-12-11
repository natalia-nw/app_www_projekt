import datetime
from rest_framework import serializers
from .models import Gatunek, Gra, Wypozyczenie, Wypozyczajacy, Komentarz


class GatunekSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gatunek
        fields = ['id', 'nazwa', 'opis']
        read_only_fields = ['id']

        def update(self, instance, validated_data):
            instance.nazwa = validated_data.get('nazwa', instance.nazwa)
            instance.opis = validated_data.get('opis', instance.opis)
            instance.save()
            return instance


class GraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gra
        fields = ['id', 'tytul', 'wydawnictwo', 'gatunek', 'min_gracze', 'max_gracze', 'opis']
        read_only_fields = ['id']

        def update(self, instance, validated_data):
            instance.tytul = validated_data.get('tytul', instance.tytul)
            instance.wydawnictwo = validated_data.get('wydawnictwo', instance.wydawnictwo)
            instance.gatunek = validated_data.get('gatunek', instance.gatunek)
            instance.min_gracze = validated_data.get('min_gracze', instance.min_gracze)
            instance.max_gracze = validated_data.get('max_gracze', instance.max_gracze)
            instance.opis = validated_data.get('opis', instance.opis)
            instance.save()
            return instance


class WypozyczajacySerializer(serializers.ModelSerializer):
    class Meta:
        model = Wypozyczajacy
        fields = ['id', 'imie', 'nazwisko', 'nr_telefonu']
        read_only_fields = ['id']

        def validate_imie(self, value):
            if not value.isalpha():
                raise serializers.ValidationError("Imię może zawierać tylko litery", )
            return value

        def validate_nazwisko(self, value):
            if not value.isalpha():
                raise serializers.ValidationError("Nazwisko może zawierać tylko litery", )
            return value

        def validate_nr_telefonu(self, value):
            if not value.isnumeric():
                raise serializers.ValidationError("Numer telefonu może zawierać tylko cyfry", )
            return value

        def update(self, instance, validated_data):
            instance.imie = validated_data.get('imie', instance.imie)
            instance.nazwisko = validated_data.get('nazwisko', instance.nazwisko)
            instance.nr_telefonu = validated_data.get('nr_telefonu', instance.nr_telefonu)
            instance.save()
            return instance


class WypozyczenieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wypozyczenie
        fields = ['id', 'gra', 'wypozyczajacy', 'data_wypozyczenia', 'uwagi']
        read_only_fields = ['id']

        def validate_data_wypozyczenia(self, data_wypozyczenia):
            if data_wypozyczenia > datetime.date.today():
                raise serializers.ValidationError("Data nie może być z przyszłości")
            return data_wypozyczenia

        def update(self, instance, validated_data):
            instance.gra = validated_data.get('gra', instance.gra)
            instance.wypozyczajacy = validated_data.get('wypozyczajacy', instance.wypozyczajacy)
            instance.data_wypozyczenia = validated_data.get('data_wypozyczenia', instance.data_wypozyczenia)
            instance.uwagi = validated_data.get('uwagi', instance.uwagi)
            instance.save()
            return instance


class KomentarzSerializer(serializers.ModelSerializer):
    class Meta:
        model = Komentarz
        fields = ['id', 'wypozyczajacy', 'gra', 'tresc', 'ocena']
        read_only_fields = ['id']

        def update(self, instance, validated_data):
            instance.wypozyczajacy = validated_data.get('wypozyczajacy', instance.wypozyczajacy)
            instance.gra = validated_data.get('gra', instance.gra)
            instance.tresc = validated_data.get('tresc', instance.tresc)
            instance.ocena = validated_data.get('ocena', instance.ocena)
            instance.save()
            return instance
