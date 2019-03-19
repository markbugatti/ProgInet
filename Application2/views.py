from django.shortcuts import HttpResponse

# Create your views here.

def product(request):
    return HttpResponse('application2/product')


def poroduct2019(request):
    return HttpResponse('poroduct2019')

def productFour(request, year, month ,day):
    return HttpResponse(
        {
            'string with format Application2/%s' % year,
            '/%s' % month,
            '/%s' % day

        }

    )
