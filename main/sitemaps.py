from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from main.models import Classe, Spell, Feat, Enhancement, Item, Race, Handbook  # Ajuste os nomes conforme seus models

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
        return reverse('classe', args=[obj.slug])  # ou obj.id se for id, ajuste conforme o campo correto


class SpellSitemap(Sitemap):
    priority = 0.6
    changefreq = 'monthly'

    def items(self):
        return Spell.objects.all()

    def location(self, obj):
        return reverse('spell', args=[obj.id])  # ajuste conforme seu campo


class FeatSitemap(Sitemap):
    priority = 0.6
    changefreq = 'monthly'

    def items(self):
        return Feat.objects.all()

    def location(self, obj):
        return reverse('feat', args=[obj.id])


class EnhancementSitemap(Sitemap):
    priority = 0.6
    changefreq = 'monthly'

    def items(self):
        return Enhancement.objects.all()

    def location(self, obj):
        return reverse('enhancement', args=[obj.name])  # ou slug/id, ajuste conforme


class ItemSitemap(Sitemap):
    priority = 0.6
    changefreq = 'monthly'

    def items(self):
        return Item.objects.all()

    def location(self, obj):
        return reverse('items')  # Se tiver uma URL específica, use ela, senão ajuste aqui


class RaceSitemap(Sitemap):
    priority = 0.6
    changefreq = 'monthly'

    def items(self):
        return Race.objects.all()

    def location(self, obj):
        return reverse('races')  # Se tiver detalhe individual, ajuste aqui


class HandbookSitemap(Sitemap):
    priority = 0.6
    changefreq = 'monthly'

    def items(self):
        return Handbook.objects.all()

    def location(self, obj):
        return reverse('handbook', args=[obj.slug])  # Ajuste para o campo correto
