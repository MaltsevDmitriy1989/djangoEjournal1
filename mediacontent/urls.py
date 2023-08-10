from django.urls import include, path

from mediacontent.views import (AboutcenterView, AboutcityView, ClubsView,
                                ContactView, IndexView, NewsView, SportView)

app_name = 'mediacontent'

urlpatterns = [
    path('news/', NewsView.as_view(), name='news'),
    path('sport/', SportView.as_view(), name='sport'),
    path('clubs/', ClubsView.as_view(), name='clubs'),
    path('aboutcity/', AboutcityView.as_view(), name='aboutcity'),
    path('aboutcenter/', AboutcenterView.as_view(), name='aboutcenter'),
    path('contact/', ContactView.as_view(), name='contact'),

]
