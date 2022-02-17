from tabnanny import verbose
from django.contrib.auth.models import AbstractUser
from django.db import models


class Employee(AbstractUser):
    first_name = models.CharField("Имя", max_length=32)
    middle_name = models.CharField("Отчество", max_length=32)
    last_name = models.CharField("Фамилия", max_length=32)
    phone = models.CharField("Телефон", max_length=16)

    def __str__(self) -> str:
        return f"{self.last_name} {self.first_name[0]}. {self.middle_name[0]}."

    class Meta:
        db_table = 'employees'
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class EmployeeRank(models.Model):
    STATUS_CHOICES = (
        ('the-best', 'Лучший'),
        ('trainee', 'Стажер'),
        ('employee', 'Сотрудник'),
    )

    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    status = models.CharField("Статус", max_length=255, choices=STATUS_CHOICES)
    description = models.TextField("Описание")

    def __str__(self) -> str:
        return f"{self.employee} - {self.status}"

    class Meta:
        db_table = 'employees_rank'
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинг"
