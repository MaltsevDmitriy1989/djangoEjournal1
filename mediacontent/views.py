from django.shortcuts import render
from django.views.generic.base import TemplateView

from common.views import TitleMixin

# Create your views here.

class IndexView(TitleMixin, TemplateView):
    template_name = 'mediacontent/index.html'
    title = 'Образовательный центр Когалым'
    greeting = 'Электронный журнал Оцелот'
    name = 'Образовательный центр города Когалым'

class NewsView(TitleMixin, TemplateView):
    template_name = 'mediacontent/news.html'
    title = 'Новости'
    greeting = 'Электронный журнал Оцелот'
    name = 'Образовательный центр города Когалым'

class SportView(TitleMixin, TemplateView):
    template_name = 'mediacontent/sports.html'
    title = 'Спорт'
    greeting = 'Электронный журнал Оцелот'
    name = 'Образовательный центр города Когалым'

class ClubsView(TitleMixin, TemplateView):
    template_name = 'mediacontent/clubs.html'
    title = 'Клубы'
    greeting = 'Электронный журнал Оцелот'
    name = 'Образовательный центр города Когалым'

class AboutcenterView(TitleMixin, TemplateView):
    template_name = 'mediacontent/center.html'
    title = 'О центре'
    greeting = 'Электронный журнал Оцелот'
    name = 'Образовательный центр города Когалым'

class AboutcityView(TitleMixin, TemplateView):
    template_name = 'mediacontent/city.html'
    title = 'О городе'
    greeting = 'Электронный журнал Оцелот'
    name = 'Образовательный центр города Когалым'

class ContactView(TitleMixin, TemplateView):
    template_name = 'mediacontent/contact.html'
    title = 'Контакты'
    greeting = 'Электронный журнал Оцелот'
    name = 'Образовательный центр города Когалым'