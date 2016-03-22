from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'form_practice.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^form/$', 'app.views.get_name', name='get_name'),
    url(r'^post/$', 'app.views.save_post', name='save_post'),
    url(r'^post/submit/$', 'app.views.save_post_submit', name='save_post_submit'),
    # url(r'^your_name/$', 'app.views.your_name', name='your_name'),
)
