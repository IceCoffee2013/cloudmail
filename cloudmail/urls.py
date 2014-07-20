from django.conf.urls import patterns, include, url

from django.contrib import admin
from mail import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cloudmail.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/$', views.test),
    url(r'^search/', views.result),

)
