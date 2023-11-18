import datetime
from django.db import models


WYD = models.IntegerChoices('Wydawnictwa',
                            'PortalGames Rebel Galakta LuckyDuckGames Muduko NaszaKsięgarnia Phalanx G3 Trefl')

GRACZE_MIN = models.IntegerChoices('Minimalna liczba graczy',
                                   '1 2 3 4')

GRACZE_MAX = models.IntegerChoices('Maksymalna liczba graczy',
                                   '1 2 3 4 5 6 7 10+')


class Gatunek(models.Model):
    nazwa = models.CharField(max_length=30)
    opis = models.CharField(max_length=50, blank=True)

    class Meta:
        ordering = ["nazwa"]

    def __str__(self):
        return f"{self.nazwa}"


class Gra(models.Model):
    tytul = models.CharField(max_length=30)
    wydawnictwo = models.IntegerField(choices=WYD.choices, default=WYD.choices[0][0])
    gatunek = models.ForeignKey(Gatunek, null=True, blank=True, on_delete=models.SET_NULL)
    min_gracze = models.IntegerField(choices=GRACZE_MIN.choices, default=GRACZE_MIN.choices[0][0])
    max_gracze = models.IntegerField(choices=GRACZE_MAX.choices, default=GRACZE_MAX.choices[0][0])
    opis = models.CharField(max_length=70, blank=True)

    class Meta:
        ordering = ["gatunek"]

    def __str__(self):
        return f"{self.tytul}"


class Wypozyczajacy(models.Model):
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=30)
    nr_telefonu = models.CharField(max_length=30)

    class Meta:
        ordering = ["nazwisko"]

    def __str__(self):
        return '%s %s' % (self.imie, self.nazwisko)


class Wypozyczenie(models.Model):
    tytul = models.ForeignKey(Gra, null=True, blank=True, on_delete=models.SET_NULL)
    wypozyczajacy = models.ForeignKey(Wypozyczajacy, null=True, blank=True, on_delete=models.SET_NULL)
    data_wypozyczenia = models.DateField('data wypożyczenia')

    def __str__(self):
        return '%s %s' % (self.tytul, self.wypozyczajacy)

    def data(self):
        return self.data_wypozyczenia >= datetime.today()
