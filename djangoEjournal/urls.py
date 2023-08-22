from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from mediacontent.views import (AboutcenterView, AboutcityView, ClubsView,
                                ContactView, IndexView, NewsView, sport)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('mediacontent/', include('mediacontent.urls', namespace='mediacontent')),
    # path('mediacontent/', NewsView.as_view(), name='news'),
    # path('mediacontent/', SportView.as_view(), name='sport'),
    # path('mediacontent/', ClubsView.as_view(), name='clubs'),
    # path('mediacontent/', AboutcityView.as_view(), name='aboutcity'),
    # path('mediacontent/', AboutcenterView.as_view(), name='aboutcenter'),
    # path('mediacontent/', ContactView.as_view(), name='contact'),
    path('users/', include('users.urls', namespace='users')),
    path('quest/', include('quest.urls', namespace='quest')),

]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns.append(path("__debug__/", include("debug_toolbar.urls")))
