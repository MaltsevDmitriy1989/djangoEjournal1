from django.shortcuts import render
from django.views.generic.base import TemplateView
from mediacontent.models import Sports, Basket
from common.views import TitleMixin
from users.forms import UserProfileForm
from django.contrib.auth.decorators import login_required
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

def sport(request):
    sports = Sports.objects.all()
    context = {
        'title': 'Спорт',
        'greeting': 'Электронный журнал Оцелот',
        'name': 'Образовательный центр города Когалым',
        'sports': sports,
    }
    return render(request, 'mediacontent/sports.html', context)

@login_required
def basket_add(request, sport_id):
    sport = Sports.objects.get(id=sport_id).name
    user = request.user
    default_data = {'first_name': user.first_name, 'last_name': user.last_name, 'username': user.username,
                    'email': user.email, 'sport': sport}
    form = UserProfileForm(default_data)
    return render(request, 'users/profile.html', {'form': form, 'user': user})

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

class EducationView(TitleMixin, TemplateView):
    template_name = 'mediacontent/courses.html'
    title = 'Образование'
    greeting = 'Электронный журнал Оцелот'
    name = 'Образовательный центр города Когалым'