from django.urls import path, include, re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    re_path(r'^signup/$', views.signup, name='signup'),
    path('login', views.login_view, name='login'),
    # re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     views.activate, name='activate'),

    # re_path(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    # re_path(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    # re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     auth_views.password_reset_confirm, name='password_reset_confirm'),
    # re_path(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
]
