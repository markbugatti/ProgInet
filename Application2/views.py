from django.shortcuts import HttpResponse, HttpResponseRedirect

# Create your views here.

def product(request):
    return HttpResponse('application2/product')


def poroduct2019(request):
    return HttpResponse('poroduct2019')

def productFour(request, year):
    return HttpResponse(
        {
            'It’s year basic folder %s' % year
        }

    )

def productFourYM(request, year, month):
    return HttpResponse(
        {
            'It’s months basic folder %s' % year,
            '%s' % month
        }

    )

def productFourYMD(request, year, month ,day):
    return HttpResponse(
            'It’s days basic folder %s/%s/%s' % (year, month, day)
    )

def productText(request, word):
    return HttpResponse(
        {
            'Your argument is %s' %word

         }
    )

def folder(request):
    return HttpResponseRedirect("/Application2/folder/Product1")

def ReFolder(request , num = "1"):
    if num == "1":
        return HttpResponse('First product page')

def folderProductN(request , numberPage):
    return HttpResponse('Product page with number %s' %numberPage)