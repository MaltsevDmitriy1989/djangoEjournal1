from django.urls import include, path
from mediacontent.views import basket_add, sport
from mediacontent.views import (AboutcenterView, AboutcityView, ClubsView,
                                ContactView, IndexView, NewsView, EducationView)

app_name = 'mediacontent'

urlpatterns = [
    path('news/', NewsView.as_view(), name='news'),
    path('sport/', sport, name='sport'),
    path('clubs/', ClubsView.as_view(), name='clubs'),
    path('aboutcity/', AboutcityView.as_view(), name='aboutcity'),
    path('aboutcenter/', AboutcenterView.as_view(), name='aboutcenter'),
    path('education/', EducationView.as_view(), name='education'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('baskets/add/<int:sport_id>/', basket_add, name='basket_add'),

]
