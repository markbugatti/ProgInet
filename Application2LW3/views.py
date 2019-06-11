from django.shortcuts import render, HttpResponse

# Create your views here.

def application2( request) :
    return HttpResponse('application2');

def index (request) :
    year = [2017, 2018, 2019, 2020, 2021]
    contact = {
        'nickname': 'markbugatti',
        'phone': '+380671687993',
    }
    context = {
        'name': 'Mark' ,
        'lastname': 'Kravchenko',
        'job_year': year,
        'contact': contact,
        'email': 'supermark11@gmail.com'
    }
    return render(request, "index.html", context);

def condition (request) :
    context = {
        'days' : [1, 2, 3, 4, 5, 6, 7],
        'current_user' : 'admin',
        'day' : 3,
        'status' : 'online',
        'email' : 'supermark11@gmail.com'
    }
    return render(request, 'condition.html', context);

def menu (request) :
    return render(request, 'menu.html');

def content (request) :
    return render(request, 'content.html');