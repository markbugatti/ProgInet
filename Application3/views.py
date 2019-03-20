from django.shortcuts import render, HttpResponse, HttpResponseRedirect

def review(request , Page):
    return HttpResponseRedirect("/Application3/review")

def reviewPage(request , Page):
    return HttpResponse('You are reading reviews page %s' %Page)
# Create your views here.
