from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import (
    Classe,
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


class ClasseSitemap(Sitemap):
    priority = 0.6
    changefreq = 'monthly'

    def items(self):
        return Classe.objects.all()

    def location(self, obj):
        return reverse('classe', args=[obj.Class])  # ajuste se usar slug ou id, aqui usei o campo Class


class RaceSitemap(Sitemap):
    priority = 0.6
    changefreq = 'monthly'

    def items(self):
        return Race.objects.all()

    def location(self, obj):
        return reverse('races')  # Se você não tem detalhe de raça individual, apenas a lista


class ItemsSitemap(Sitemap):
    priority = 0.6
    changefreq = 'monthly'

    def items(self):
        return Items.objects.all()

    def location(self, obj):
        return reverse('items')  # Se tiver página detalhada, ajuste para args=[obj.id] ou algo assim


class FeatsSitemap(Sitemap):
    priority = 0.6
    changefreq = 'monthly'

    def items(self):
        return Feats.objects.all()

    def location(self, obj):
        return reverse('feat', args=[obj.id])  # Ajuste se o nome da URL e parâmetro for diferente


class SpellsSitemap(Sitemap):
    priority = 0.6
    changefreq = 'monthly'

    def items(self):
        return Spells.objects.all()

    def location(self, obj):
        return reverse('spell', args=[obj.id])  # Ajuste se necessário


class EnhancementsSitemap(Sitemap):
    priority = 0.6
    changefreq = 'monthly'

    def items(self):
        return Magic_Enhancement.objects.all()

    def location(self, obj):
        return reverse('enhancement', args=[obj.name])  # Ajuste para slug/id se usar


class HandbooksSitemap(Sitemap):
    priority = 0.6
    changefreq = 'monthly'

    def items(self):
        return Handbooks.objects.all()

    def location(self, obj):
        return reverse('handbook', args=[obj.text])  # Ajuste para campo correto, aqui usei text

