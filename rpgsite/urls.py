from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from main.sitemaps import (
    StaticViewSitemap,
    ClasseSitemap,
    SpellSitemap,
    FeatSitemap,
    EnhancementSitemap,
    ItemSitemap,
    RaceSitemap,
    HandbookSitemap,
)

sitemaps = {
    'static': StaticViewSitemap,
    'classes': ClasseSitemap,
    'spells': SpellSitemap,
    'feats': FeatSitemap,
    'enhancements': EnhancementSitemap,
    'items': ItemSitemap,
    'races': RaceSitemap,
    'handbooks': HandbookSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('users/', include('users.urls')),
    path('tools/', include('tools.urls')),
    path('captcha/', include('captcha.urls')),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
