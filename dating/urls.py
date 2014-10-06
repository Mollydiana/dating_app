from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'dating_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^register/$', 'dating_app.views.register', name='register'),
    url(r"^payments/", include("payments.urls")),
    url(r'^questions/$', 'dating_app.views.questions', name='questions'),
    url(r'^video/$', 'dating_app.views.video', name='video'),
    url(r'^theone/$', 'dating_app.views.theone', name='theone'),


    # url(r'^charge/', 'dating_app.views.charge', name='charge'),



    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^payment/$', 'dating_app.views.payment', name='payment'),



    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),


    url(r'^admin/', include(admin.site.urls)),
)
