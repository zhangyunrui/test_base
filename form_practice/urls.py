from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^form/$', 'app.views.get_name', name='get_name'),
                       url(r'^post/$', 'app.views.save_post', name='save_post'),
                       url(r'^post/submit/$', 'app.views.save_post_submit', name='save_post_submit'),
                       )
