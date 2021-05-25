from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='client_photo/')
    phone = models.CharField(max_length=11)

    def __str__(self):
        return "Клиент: {}, телефон: {}".format(self.user, self.phone)


class Company(models.Model):
    COMPANY_TYPE = [
        ('1', 'Салон красоты'),
        ('2', 'Автосервис'),
        ('3', 'Маникюрный салон'),
        ('4', 'Медицинский центр'),
        ('5', 'Сервисный центр')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='company_logo/')
    type = models.CharField(choices=COMPANY_TYPE, default='1', max_length=1)

    def __str__(self):
        return "Организация: {}, тип: {}".format(self.user, self.get_type_display())


class Office(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone = PhoneNumberField()
    schedule = models.CharField(max_length=255)

    def __str__(self):
        return "Филиал организации: {}, адрес: {}".format(self.company, self.address)


class Position(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return "Должность: {}".format(self.name)


class Employee(models.Model):
    office = models.ForeignKey(Office, on_delete=models.SET_NULL, null=True)
    position = models.ManyToManyField(Position)
    fio = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='employee_photo/', null=True, blank=True)

    def __str__(self):
        return "Работник: {}, должность: {}".format(self.fio, self.position.all())


class Service(models.Model):
    office = models.ManyToManyField(Office)
    name = models.CharField(max_length=255)
    duration = models.FloatField(null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return "Услуга: {} в филиале {}".format(self.name, self.office.all())


class ServicePosition(models.Model):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    price = models.FloatField(default=0)

    class Meta:
        unique_together = (("position", "service"), )

    def __str__(self):
        return "Услуга по должности: {}, {}".format(self.service, self.position)


class Entry(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    office = models.ForeignKey(Office, on_delete=models.SET_NULL, null=True)
    created_datetime = models.DateTimeField()

    def __str__(self):
        return "Запись: клиент: {}, работник: {}, услуга: {}, филиал: {}".format(self.client, self.employee,
                                                                                 self.service, self.office)
