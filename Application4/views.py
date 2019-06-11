from django.shortcuts import render, HttpResponse, HttpResponseRedirect

def application4(request):
    return  HttpResponse('Application4')

def redirect(request):
    return  HttpResponseRedirect('/Application4/redirected')

def redirected(request):
    return HttpResponse('You were redirected');

def renderHtml(requdest):
    _html = "<!DOCTYPE html><html><body><h1>My First Heading</h1><p>My first paragraph.</p></body></html>";
    return HttpResponse(_html);
def htmlFormTemplate(request):
    return render(request, "form1.html");

def formHandler(request):
    if (request.POST):
        return HttpResponse("Method: Post" );
    else:
        return HttpResponse("Method: Get");

# Create your views here.