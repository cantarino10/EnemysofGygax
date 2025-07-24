from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import (
    Classes,           # plural: é o model correto para classes
    Race,
    Items,
    Feats,
    Spells,
    Magic_Enhancement,
    Handbooks,
)

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return [
            'index',
            'handbooks',
            'races',
            'classes',
            'items',
            'feats',
            'spells',
            'enhancements',
            'roll_dice',
            'stats_builder',
            'encounter',
            'login',
            'register',
            'password_reset',
        ]

    def location(self, item):
        return reverse(item)


class ClassesSitemap(Sitemap):    # plural, corresponde ao model Classes
    priority = 0.6
    changefreq = 'monthly'

    def items(self):
        return Classes.objects.all()

    def location(self, obj):
        return reverse('classe', args=[obj.text])  # ajuste para o campo correto


class RaceSitemap(Sitemap):
    priority = 0.6
    changefreq = 'monthly'

    def items(self):
        return Race.objects.all()

    def location(self, obj):
        return reverse('race', args=[obj.Race])  # se tiver página detalhada


class ItemsSitemap(Sitemap):
    priority = 0.6
    changefreq = 'monthly'

    def items(self):
        return Items.objects.all()

    def location(self, obj):
        return reverse('item', args=[obj.id])  # se tiver página detalhada


class FeatsSitemap(Sitemap):
    priority = 0.6
    changefreq = 'monthly'

    def items(self):
        return Feats.objects.all()

    def location(self, obj):
        return reverse('feat', args=[obj.id])  # ajuste se necessário


class SpellsSitemap(Sitemap):
    priority = 0.6
    changefreq = 'monthly'

    def items(self):
        return Spells.objects.all()

    def location(self, obj):
        return reverse('spell', args=[obj.id])


class EnhancementsSitemap(Sitemap):
    priority = 0.6
    changefreq = 'monthly'

    def items(self):
        return Magic_Enhancement.objects.all()

    def location(self, obj):
        return reverse('enhancement', args=[obj.name])  # ou outro campo identificador


class HandbooksSitemap(Sitemap):
    priority = 0.6
    changefreq = 'monthly'

    def items(self):
        return Handbooks.objects.all()

    def location(self, obj):
        return reverse('handbook', args=[obj.text])  # ou outro campo identificador
