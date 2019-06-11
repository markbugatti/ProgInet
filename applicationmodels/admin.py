from django.contrib import admin
from .models import Example, Author, Book, Place, Restaurant, Waiter, Publication, Article

# Register your models here.

admin.site.register(Example)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname')
    list_filter = ('name', 'surname')
admin.site.register(Author, AuthorAdmin)

admin.site.register(Book)
admin.site.register(Place)
admin.site.register(Restaurant)
admin.site.register(Waiter)
admin.site.register(Publication)
admin.site.register(Article)