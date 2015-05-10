from django.conf.urls import patterns, include, url
from django.contrib import admin

# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'booki.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),

#     url(r'^booklist/', include('booklist.urls')),
#     url(r'^admin/', include(admin.site.urls)),
# )

urlpatterns = [
    url(r'^booklist/', include('booklist.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
