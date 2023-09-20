from django import forms
from django.db import models

class Creat_form(forms.Form):
    name = forms.CharField(label='Введите имя')

    list_gender = (('мужской', 'М'), ('женский', 'Ж'))
    gender = forms.TypedChoiceField(label='Пол:', choices=list_gender)

    list_age = (('молодой', '5-20'), ('средний', '20-50'), ('пожилой', '50-100'))
    age = forms.TypedChoiceField(label='Возраст:', choices=list_age)

    list_habits = (('нет', 'нет'), ('курю', 'К'), ('бухаю', 'Б'), ('курю-бухаю', 'КБ'))
    habist = forms.TypedChoiceField(label='Вредные привычки:', choices=list_habits)

    list_language = (('русский', 'RU'), ('английский', 'ANG'), ('французкий', 'FR'))
    language = forms.TypedChoiceField(label='Язык:', choices=list_language)

    E_mail = forms.EmailField(label='E-mail')

    skil_food = forms.NullBooleanField(label='Умеете готовить?')

    availability_cat = forms.BooleanField(label='У вас есть кот?')

    img = forms.ImageField(label='Фото')

    list_background_color = ('зеленый', 'Зел'), ('синий', 'Син'), ('оранжевый', 'Оранж')
    background_color = forms.TypedChoiceField(label='Фоновый цвет:', choices=list_background_color)
