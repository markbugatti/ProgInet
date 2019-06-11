from django.db import models

# Create your models here.

class Example (models.Model) :
    integ = models.IntegerField
    posInt = models.PositiveIntegerField
    posSmInt = models.PositiveSmallIntegerField
    bgInt = models.BigIntegerField
    ft = models.FloatField
    bn = models.BinaryField
    bl = models.BooleanField
    ch = models.CharField('Ім\'я', max_length=5)
    txt = models.TextField('Про мене:', max_length=20)
    date = models.DateField('Дата народження:', auto_now=False)
    dateTime = models.DateTimeField('Початок роботи:', auto_now_add=False)
    dc = models.DecimalField('Трудова оцінка:', max_digits=8, decimal_places=2)
    em = models.EmailField('Електрона адреса:')
    fl = models.FileField
    img = models.ImageField

    class Meta:
        verbose_name = "Співробітники"
        verbose_name_plural = "Співробітники"

    def __str__(self):
        return '%s' % (self.ch)

class Author (models.Model) :
    name =  models.CharField("Ім'я",max_length=50)
    surname = models.CharField("Прізвище",max_length=50)
    birthday = models.DateField(auto_now=False)

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Автори"

    def __str__(self):
        return 'Ім\'я: %s, Прізвище: %s' % (self.name, self.surname)

# Genre = [
#     ('classic', 'Класика')
#     ('detective', 'Детектив')
#     ('novel', 'Роман')
#     ('fantasy', 'Фантастика')
#     ('adventure', 'Пригоди')
# ]

class Book (models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    descrition = models.TextField(max_length=1000)
    # list
    Genre = [
        ('classic', 'Класика'),
        ('detective', 'Детектив'),
        ('novel', 'Роман'),
        ('fantasy', 'Фантастика'),
        ('adventure', 'Пригоди'),
    ]

    genre = models.CharField(
        max_length=50,
        choices=Genre,
        default='classic'
    )

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return '%s' % (self.name)

class Place (models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Місце"
        verbose_name_plural = "Місця"

    def __str__(self):
        return '%s' % (self.name)

class Restaurant (models.Model):
    place = models.OneToOneField(Place, on_delete=models.CASCADE)
    delivery = models.BooleanField(default=False)
    allDay = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Ресторан"
        verbose_name_plural = "Ресторани"

    def __str__(self):
        return '%s' % (self.place.name)

class Waiter (models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Офіціант"
        verbose_name_plural = "Офіціанти"

    def __str__(self):
        return 'Офіціант: %s, Ресторан: %s' % (self.name, self.restaurant.place.name)

class Publication (models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Видання"
        verbose_name_plural = "Видання"


    def __str__(self):
        return '%s' % (self.name)

class Article (models.Model):
    name = models.CharField(max_length=50)
    publication = models.ManyToManyField(Publication)

    class Meta:
        verbose_name = "Стаття"
        verbose_name_plural = "Статті"

    def __str__(self):
        return '%s' % (self.name)