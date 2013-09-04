from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.contrib.auth.models import User, Group
from home.models import Job, WebsiteUser

from rest_framework import viewsets, routers

class UserViewSet(viewsets.ModelViewSet):
    model = User

class WebsiteUserViewSet(viewsets.ModelViewSet):
    model = WebsiteUser

class GroupViewSet(viewsets.ModelViewSet):
    model = Group

class JobViewSet(viewsets.ModelViewSet):
    model = Job

# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'website users', WebsiteUserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'jobs', JobViewSet)

# Wire up API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
    url(r'^home.*$', 'home.views.home', name='home'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^rest/', include('rest_framework.urls', namespace='rest_framework')),
)

