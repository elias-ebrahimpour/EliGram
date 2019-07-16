"""eligram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from django.conf.urls import url, include
from django.urls import path, include
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

admin.site.index_title = _('Elias Ebrahimpour')
admin.site.site_header = _('EliGram')
admin.site.site_title = _('مدیریت جنگو')

sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('images/', include('images.urls', namespace='images')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('social_auth/', include('social_django.urls', namespace='social')),
    prefix_default_language=False
)
