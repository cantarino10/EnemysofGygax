from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from urllib.parse import quote

from .models import Classes, Race, Items, Feats, Spells, Magic_Enhancement, Handbooks

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return [
            'index', 'handbooks', 'races', 'classes', 'items', 'feats', 'spells',
            'enhancements', 'roll_dice', 'stats_builder', 'encounter',
            'login', 'register', 'password_reset',
        ]

    def location(self, item):
        return reverse(item)

class ClassesSitemap(Sitemap):
    priority = 0.6
    changefreq = 'monthly'

    def items(self):
        return Classes.objects.all()

    def location(self, obj):
        return reverse('classe', args=[quote(obj.text, safe='')])

class RaceSitemap(Sitemap):
    priority = 0.6
    changefreq = 'monthly'

    def items(self):
        return Race.objects.all()

    def location(self, obj):
        return reverse('race', args=[quote(obj.Race, safe='')])

class ItemsSitemap(Sitemap):
    priority = 0.6
    changefreq = 'monthly'

    def items(self):
        return Items.objects.all()

    def location(self, obj):
        return reverse('item', args=[obj.id])

class FeatsSitemap(Sitemap):
    priority = 0.6
    changefreq = 'monthly'

    def items(self):
        return Feats.objects.all()

    def location(self, obj):
        return reverse('feat', args=[obj.id])

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
        return reverse('enhancement', args=[quote(obj.name, safe='')])

class HandbooksSitemap(Sitemap):
    priority = 0.6
    changefreq = 'monthly'

    def items(self):
        return Handbooks.objects.all()

    def location(self, obj):
        return reverse('handbook', args=[quote(obj.text, safe='')])
