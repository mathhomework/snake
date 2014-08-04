from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'games.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'snake.views.home', name='home'),
    url(r'^login/', 'django.contrib.auth.views.login', name = "login"),
    url(r'^register/', 'snake.views.register', name = "register"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name = "logout"),
    url(r'^profile/$', 'snake.views.profile', name = "profile"),

)