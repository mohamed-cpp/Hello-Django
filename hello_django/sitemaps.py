from django.contrib import sitemaps
from django.urls import reverse

from .utils.url import underscored_name
from admins.models import Admin

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['admins']

    def location(self, item):
        return reverse(item)

class AdminSitemap(sitemaps.Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'http'

    def items(self):
        return Admin.objects.all()

#    def lastmod(self, obj):
#        return obj.created_at

    def location(self,obj):
        return reverse('adminroute', args=(underscored_name(obj.name), obj.id))
        #return "/perfix/admin/show/%s/%s" % (self.underscored_name(obj.name), obj.id)