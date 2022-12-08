from django.db import models

class Branch(models.Model):
    position = models.CharField(max_length=30)
    department = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.position} - {self.department}'


class Employees(models.Model):
    name = models.CharField(max_length=30)
    birth_date = models.DateField()
    position = models.ForeignKey(Branch, on_delete=models.CASCADE)
    salary = models.IntegerField()

    def __str__(self):
        return f'{self.name} - {self.position.position}'

