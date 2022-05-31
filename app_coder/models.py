from django.db import models


class Sucursal(models.Model):
    name = models.CharField(max_length=40)
    code = models.IntegerField()

    def __str__(self):
        return f'{self.name} sucursal --'


class Vendedor(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    area = models.CharField(max_length=40)

    def __str__(self):
        return f'Nombre del vendedor: {self.name} {self.last_name} -- e-mail: {self.email} -- area: {self.area} --'


class Producto(models.Model):
    name = models.CharField(max_length=40)
    due_date = models.DateField()
    is_delivered = models.BooleanField()

    def __str__(self):
        is_delivered = 'Si' if self.is_delivered else 'No'
        return f'Nombre del producto: {self.name} -- Fecha de elaboración: {self.due_date} -- Vendido: {is_delivered}'
