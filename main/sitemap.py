from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Handbook, Classe, Spell, Feat  # ou os nomes corretos

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return ['index', 'classes', 'races', 'spells', 'items', 'enhancements', 'handbooks']

    def location(self, item):
        return reverse(item)

class HandbookSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return Handbook.objects.all()

    def location(self, obj):
        return reverse('handbook', args=[obj.name])

# Repita para outras classes se quiser:
# ClasseSitemap, SpellSitemap, FeatSitemap, etc.
