from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.contrib import admin
 a = 2
from main.sitemaps import (
    StaticViewSitemap,
    ClassesSitemap,
    RaceSitemap,
    ItemsSitemap,
    FeatsSitemap,
    SpellsSitemap,
    EnhancementsSitemap,
    HandbooksSitemap,
)

sitemaps = {
    'static': StaticViewSitemap,
    'classes': ClassesSitemap,
    'races': RaceSitemap,
    'items': ItemsSitemap,
    'feats': FeatsSitemap,
    'spells': SpellsSitemap,
    'enhancements': EnhancementsSitemap,
    'handbooks': HandbooksSitemap,
}
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('users/', include('users.urls')),
    path('tools/', include('tools.urls')),
    path('captcha/', include('captcha.urls')),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
