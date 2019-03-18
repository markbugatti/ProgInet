from django.shortcuts import HttpResponse

# Create your views here.

def product(request):
    return HttpResponse('application2/product')
