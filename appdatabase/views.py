from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.generic.base import TemplateView
from .models import Human

# Create your views here.

def appdatabase(request):
    return HttpResponse('appdatabase')

class List (TemplateView):
    template_name = 'list.html'
    model = Human

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['human_list'] = Human.objects.all()
        # first three
        context['firstThree_list'] = Human.objects.all()[:3]
        context['first_company'] = Human.objects.filter(company='Epam')
        context['after_year_00'] = Human.objects.filter(birth__year__gte=2000)
        context['first_human'] = Human.objects.filter(id__exact=1)
        context['birth_desc'] = Human.objects.order_by('-birth')
        context['salary_less_2000'] = Human.objects.filter(salary__lt=2000)
        context['salary_asc'] = Human.objects.order_by('salary')
        context['name_exact'] = Human.objects.filter(name='Alex')

        # humanList = Human.objects.all()
        # firstThreeList = Human.objects.all()[:3]
        # firstCompany = Human.objects.filter(company='Epam')
        # afterYear00 = Human.objects.filter(birth__year__gte=2000)
        # firstHuman = Human.objects.filter(id__exact=1)
        # birthDesc = Human.objects.order_by('-birth')
        # salaryLess_2000 = Human.objects.filter(salary__lt=2000)
        # salaryAsc = Human.objects.order_by('salary')
        #
        # context : {
        #     'human_list' : humanList,
        #     'firstThree_list' : firstThreeList,
        #     'first_company' : firstCompany,
        #     'after_year_0' : afterYear00,
        #     'first_human' : firstHuman,
        #     'birth_desc' : birthDesc,
        #     'salary_less_2000' : salaryLess_2000,
        #     'salary_asc' : salaryAsc,
        # }

        return context


