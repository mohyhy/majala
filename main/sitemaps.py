from django.contrib.sitemaps import Sitemap
from django.contrib import sitemaps
from django.urls import reverse
from .models import New

class StaticSitemap(sitemaps.Sitemap):
    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return New.objects.all()
    def location(self, item):
        return item
    



# class ProductSitemap(Sitemap):

#     def items(self):
#         return New.objects.all()

#     def location(self, item):
#         return reverse('main:page', args=[item.page_title])    