from random import randint, choice
from django.http import HttpResponse
import logging
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .forms import GameForm


logger = logging.getLogger(__name__)


def lesson4(request):
    return HttpResponse("<h3>Seminar 4</h3>")


def heads_tails(request, n):
    # logger.info(f'{request}heads_tails page accessed')
    context = {"res": []}
    for _ in range(n):
        context['res'].append(choice(['Heads', 'Tails']))
    return render(request, 'lesson_4_app/gameplay.html', context)


def dice(request, n):
    context = {"res": []}
    for _ in range(n):
        context['res'].append(randint(1, 6))
    return render(request, 'lesson_4_app/gameplay.html', context)


def rand(request, n):
    context = {"res": []}
    for _ in range(n):
        context['res'].append(randint(1, 100))
    return render(request, 'lesson_4_app/gameplay.html', context)

# Доработаем задачу про броски монеты, игральной кости и случайного числа.
# 📌 Создайте форму, которая предлагает выбрать: монета, кости, числа.
# 📌 Второе поле предлагает указать количество попыток от 1 до 64.

def games(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            count = int(form.cleaned_data['count'])
            logger.info(f'count={count} from game {form.cleaned_data["choice"]} accessed')
            match form.cleaned_data['choice']:
                case '1':
                    return heads_tails(request, count)
                case '2':
                    return dice(request, count)
                case '3':
                    return rand(request, count)
    else:
        logger.info(f'Get new form')
        form = GameForm()
    return render(request, 'lesson_4_app/games_form.html', {'form': form})

# Продолжаем работу с авторами, статьями и комментариями.
# 📌 Создайте форму для добавления нового автора в базу
# данных.
# 📌 Используйте ранее созданную модель Author

# def create_author(request):
#     if request.method == 'POST':
#         form = AuthorForms(request.POST)
#         if form.is_valid():
#             author = Author(f_name=form.cleaned_data['name'],
#                             l_name=form.cleaned_data['surname'],
#                             email=form.cleaned_data['email'],
#                             biography=form.cleaned_data['biography'],
#                             birthday=form.cleaned_data['birthday'])
#             author.save()
#             # massages.add_message(request, messages.SUCCESS, 'Successfully')
#         else:
#             form = AuthorForms()
#         return render(request, 'autor_form.html', {'form': form})