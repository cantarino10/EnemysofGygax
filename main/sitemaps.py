from django.contrib.sitemaps import Sitemap
from django.urls import reverse

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
            # URLs que não precisam de parâmetro
            'roll_dice',
            'stats_builder',
            'encounter',
            'login',
            'register',
            'password_reset',
        ]

    def location(self, item):
        return reverse(item)
