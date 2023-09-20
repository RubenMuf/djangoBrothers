from django.http import HttpResponse
from django.shortcuts import render
from Brothers.creat_form import Creat_form

# Create your views here.

def index(request):
    return render(request, 'home.html')

def socsety(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        habist = request.POST.get('habist')
        age = request.POST.get('age')
        language = request.POST.get('language')
        E_mail = request.POST.get('E_mail')
        skil_food = request.POST.get('skil_food')
        availability_cat = request.POST.get('availability_cat')
        background_color = request.POST.get('background_color')
        # print(background_color)
        if background_color == 'зеленый':
            color = 'green'
            print(color)
        elif background_color == 'синий':
            color = 'blue'
        elif background_color == 'оранжевый':
            color = 'orange'
        # print(name, age, language, E_mail, skil_food, availability_cat, sep='\n')

        # сохраняем картинку
        img = request.FILES.get('img').read()
        file = open(f'famile/static/upload/{name}.jpg', 'wb')
        file.write(img)
        # загружаем на страницу
        foto = f'upload/{name}.jpg'
        data = {'img': foto,
                'name': name,
                'age': age,
                'gender': gender,
                'habist': habist,
                'language': language,
                'E_mail': E_mail,
                'skil_food': skil_food,
                'availability_cat': availability_cat,
                'color': color
                }
        return render(request, 'person.html', context=data)
    else:
        anketa = Creat_form
        data = {'form': anketa}
        return render(request, 'forma.html', context=data)
