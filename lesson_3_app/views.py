from django.shortcuts import render
from random import randint, choice
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def about(request):
    a = "About me:"
    b = "I am a student GB"
    return render(request, 'lesson_3_app/about_me.html', {"a": a, "b": b})

# Доработаем задачу 7 из урока 1, где бросали монетку, игральную кость и генерировали случайное число.
# 📌 Маршруты могут принимать целое число - количество бросков.
# 📌 Представления создают список с результатами бросков и передают его в контекст шаблона.
# 📌 Необходимо создать универсальный шаблон для вывода результатов любого из трёх представлений.

def heads_tails(request, n):
    # logger.info(f'{request}heads_tails page accessed')
    context = {"res": []}
    # n = int(request.GET.get('n', '5'))
    for _ in range(n):
        context['res'].append(choice(['Heads', 'Tails']))
    return render(request, 'lesson_3_app/gameplay.html', context)

def dice(request, n):
    # logger.info(f'{request}heads_tails page accessed')
    context = {"res": []}
    # n = int(request.GET.get('n', '5'))
    for _ in range(n):
        context['res'].append(randint(1, 6))
    return render(request, 'lesson_3_app/gameplay.html', context)

def rand(request, n):
    # logger.info(f'{request}heads_tails page accessed')
    context = {"res": []}
    # n = int(request.GET.get('n', '5'))
    for _ in range(n):
        context['res'].append(randint(1, 100))
    return render(request, 'lesson_3_app/gameplay.html', context)

def gp(request, n):
    # logger.info(f'{request}heads_tails page accessed')
    context = {"res1": [], "res2": [], "res3": []}
    # n = int(request.GET.get('n', '5'))

    for _ in range(n):
        context['res1'].append(choice(['Heads', 'Tails']))
        context['res2'].append(randint(1, 6))
        context['res3'].append(randint(1, 100))
    return render(request, 'lesson_3_app/gp.html', context)

# Доработаем задачи из прошлого семинара по созданию моделей автора, статьи и комментария.
# 📌 Создайте шаблон для вывода всех статей автора в виде списка заголовков.
# ○ Если статья опубликована, заголовок должен быть ссылкой на статью.
# ○ Если не опубликована, без ссылки.
# 📌 Не забываем про код представления с запросом к базе данных и маршруты
# Доработаем задачу 4.
# 📌 Создай шаблон для вывода подробной информации о
# статье.
# 📌 Внесите изменения в views.py - создайте представление и в urls.py - добавьте маршрут.
# 📌 *Увеличивайте счётчик просмотра статьи на единицу при каждом простре.