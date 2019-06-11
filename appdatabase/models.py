from django.db import models

# Create your models here.

# class HumanManager(models.Manager):
#     def create_human(self, name, surname, birth, salary):
#         human = self.create(name=name,
#                             surname=surname,
#                             birth=birth,
#                             salary=salary)
#         return human

class Human (models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birth = models.DateField()
    COMPANY = (
        ('Epam', 'Epam'),
        ('Global Logic', 'Global Logic'),
        ('Microsoft', 'Microsoft'),
        ('Google', 'Google'),
        ('Amazon', 'Amazon')
    )
    company = models.CharField(max_length=150, choices=COMPANY)
    POSITION = (
        ('p', 'Programmer'),
        ('d', 'CEO'),
        ('m', 'Manager')
    )
    position = models.CharField(max_length=15, choices=POSITION)
    LANGUAGE = (
        ('e', 'English'),
        ('f', 'Franch'),
        ('g', 'German'),
        ('u', 'Ukrainian'),
        ('r', 'Russion'),
    )
    language = models.CharField(max_length=10, choices=LANGUAGE, default='e')
    salary = models.IntegerField()

    def __str__(self):
        return 'Ім\'я: %s, Прізвище: %s, Компанія: %s' % (self.name, self.surname, self.company)

    # objects = HumanManager()