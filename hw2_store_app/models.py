# Создайте три модели Django: клиент, товар и заказ.
# Клиент может иметь несколько заказов. Заказ может содержать несколько товаров.
# Товар может входить в несколько заказов.
# 📌 Поля модели "Клиент":
# ○ имя клиента
# ○ электронная почта клиента
# ○ номер телефона клиента
# ○ адрес клиента
# ○ дата регистрации клиент
# Поля модели "Товар":
# ○ название товара
# ○ описание товара
# ○ цена товара
# ○ количество товара
# ○ дата добавления товара
# Поля модели "Заказ":
# ○ связь с моделью "Клиент", указывает на клиента,
# сделавшего заказ
# ○ связь с моделью "Товар", указывает на товары, входящие в заказ
# ○ общая сумма заказа
# ○ дата оформления заказа
# 📌 *Допишите несколько функций CRUD для работы с моделями по желанию.
# Что по вашему мнению актуально в такой базе даннных

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=15)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    reg_date = models.DateField(auto_now=True)
    birthday = models.DateField(default='2000-01-01')

    def __str__(self):
        return f'Username: {self.name}, email: {self.email}, phone: {self.phone}'


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=1)
    available = models.BooleanField(default=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f' Product: {self.product_name}, price: {self.price} '


STATUS_CHOICES = [
        ('INWORK', 'in_working'),
        ('FINISHED', 'finished'),
        ('CANCELED', 'canceled'),
]

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    status = models.CharField(choices=STATUS_CHOICES, max_length=10, default='INWORK')

    def __str__(self):
        return f'order_id:{self.id}, Customer:{self.customer.name}, total_price: {self.total_price} '
