
from django.urls import path, include, re_path
from . import views

urlpatterns = [

    re_path(r'^signup/$', views.signup, name='signup'),
    path('login',views.login_view,name='login')
    # re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     views.activate, name='activate'),
]
