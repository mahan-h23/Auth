from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static
from account import urls as accounturls

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('accounts/', include(accounturls))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                                         document_root=settings.STATIC_ROOT)
