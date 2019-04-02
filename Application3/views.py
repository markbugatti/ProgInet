from django.shortcuts import render, HttpResponse, HttpResponseRedirect

def review(request , Page):
    return HttpResponseRedirect("/Application3/review")

def reviewPage(request , Page):
    return HttpResponse('You are reading reviews page %s' %Page)

def comments(request):
    return HttpResponse('First comment');

def comments_number(request, number):
    return HttpResponse('your comment has number %s' %number)

def reviewAction(request, page, action):
    if (action == 'edit'):
        return HttpResponse('You are editing page %s' %page)
    if (action == 'delete'):
        return HttpResponse('You are deleting page %s' %page)
    else:
        return HttpResponse('You are discussing page %s' % page)

# Create your views here.
