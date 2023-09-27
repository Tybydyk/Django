from django.db import models
from django.utils import timezone


# Создайте модель для запоминания бросков монеты: орёл или решка.
# 📌 Также запоминайте время броска
# Доработаем задачу 1.
# 📌 Добавьте статический метод для статистики по n последним
# броскам монеты.
# 📌 Метод должен возвращать словарь с парой ключей- значений, для орла и для решки.

class HeadsTails(models.Model):
    rest_time = models.DateTimeField(default=timezone.now)
    res = models.CharField(max_length=50)

    @staticmethod
    def statistic(n):
        n = int(n)
        dict_res = {'Heads': 0, 'Tails': 0}
        query = list(HeadsTails.objects.all())
        list_res = query[-n:]
        for item in list_res:
            if 'Heads' in str(item):
                dict_res['Heads'] += 1
            elif 'Tails' in str(item):
                dict_res['Tails'] += 1
        return dict_res

    def __str__(self):
        return f' time:{self.rest_time}, res:{self.res}'

# оздайте модель Автор. Модель должна содержать следующие поля:
# ○ имя до 100 символов
# ○ фамилия до 100 символов
# ○ почта
# ○ биография
# ○ день рождения
# 📌 Дополнительно создай пользовательское поле “полное имя”, которое возвращает имя и фамилию.
# Создайте модель Статья (публикация). Авторы из прошлой задачи могут писать статьи. У статьи может быть только один автор. У статьи должны быть следующие обязательные поля:
# ○ заголовок статьи с максимальной длиной 200 символов
# ○ содержание статьи
# ○ дата публикации статьи
# ○ автор статьи с удалением связанных объектов при удалении автора
# ○ категория статьи с максимальной длиной 100 символов
# ○ количество просмотров статьи со значением по умолчанию 0
# ○ флаг, указывающий, опубликована ли статья со значением по умолчанию False

class Author(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100, default=f_name)
    email = models.EmailField()
    biography = models.TextField(default='biography')
    birthday = models.DateField(default=timezone.now())

    def full_name(self):
        return f'{self.f_name} {self.l_name}'

    def __str__(self):
        return f'Name: {self.full_name()}, email: {self.email}'

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published = models.DateField(default=timezone.now())
    category = models.CharField(max_length=100, default='Humor')
    show_count = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f'author: {self.author.f_name} - article: {self.title} '