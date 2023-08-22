# -*- coding: UTF-8 -*-

from django import forms
from .models import *
from django.forms.models import inlineformset_factory

TOPIC_CHOICES = (
    ('general', 'General enquiry'),
    ('bug', 'Bug report'),
    ('suggestion', 'Suggestion'),
)

class question_form(forms.Form):
    key_1 = forms.CharField(label="Ключ 1", initial = "Угол поворота", widget=forms.TextInput(attrs={"class":"myfield"}))    
    key_2 = forms.CharField(label="Ключ 2", initial = "Угловая скорость", widget=forms.TextInput(attrs={"class":"myfield"}))
    key_3 = forms.CharField(label="Ключ 3", initial = "Угловое ускорение", widget=forms.TextInput(attrs={"class":"myfield"}))
    answer = forms.CharField(label="Ответ", initial = "Угловое ускорение, угловая скорость, угол поворота, радиус.", widget=forms.TextInput(attrs={"class":"myfield"}))

class code_form(forms.Form):
    code = forms.CharField(label="Код")
    def clean_code(self):
        code = self.cleaned_data.get('code', '')
        return code
