from django.contrib import admin
from .models import Gatunek, Gra, Wypozyczajacy, Wypozyczenie, Komentarz


class GatunekAdmin(admin.ModelAdmin):
    list_display = ['nazwa']
    list_filter = ['nazwa']


admin.site.register(Gatunek, GatunekAdmin)


class GraAdmin(admin.ModelAdmin):
    list_display = ['tytul', 'wydawnictwo', 'gatunek', 'gracze']
    list_filter = ['tytul', 'wydawnictwo', 'gatunek']

    @admin.display(description='gracze')
    def gracze(self, obj):
        if obj.min_gracze is not None and obj.max_gracze is None:
            return str(obj.min_gracze)
        if obj.min_gracze is None and obj.max_gracze is not None:
            return str(obj.max_gracze)
        if obj.min_gracze is not None and obj.max_gracze is not None:
            if obj.min_gracze == obj.max_gracze:
                return str(obj.min_gracze)
            if obj.min_gracze != obj.max_gracze:
                return str(obj.min_gracze) + " - " + str(obj.max_gracze)
        return " "


admin.site.register(Gra, GraAdmin)


class WypozyczenieAdmin(admin.ModelAdmin):
    list_display = ['gra', 'wypozyczajacy', 'data_wypozyczenia']
    list_filter = ['gra', 'wypozyczajacy', 'data_wypozyczenia']


admin.site.register(Wypozyczenie, WypozyczenieAdmin)


class WypozyczajacyAdmin(admin.ModelAdmin):
    list_display = ['imie', 'nazwisko', 'nr_telefonu']
    list_filter = ['nazwisko']


admin.site.register(Wypozyczajacy, WypozyczajacyAdmin)


class KomentarzAdmin(admin.ModelAdmin):
    list_display = ['gra', 'tresc', 'ocena']
    list_filter = ['gra', 'ocena']


admin.site.register(Komentarz, KomentarzAdmin)
