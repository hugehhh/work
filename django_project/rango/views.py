from django.shortcuts import render
from rango.models import Category, Page
from django.views import View
# Create your views here.

from django.http import HttpResponse


def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {
        'categories': category_list
                    }
    return render(request, 'rango/index.html', context=context_dict)


def AboutView(request):
    return HttpResponse("Nobody here")