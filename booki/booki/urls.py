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
    url(r'^$', 'booklist.views.index'),
    url(r'^booklist/', include('booklist.urls', namespace="booklist")),
    url(r'^login/$', 'django.contrib.auth.views.login', name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name="logout"),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^new-entry/', 'booklist.views.new_entry', name="new_entry")

    ]
