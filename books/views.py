from django.views.generic import TemplateView, ListView, DetailView 
from django.shortcuts import render
from .models import Manufactures, Categories, Products

class HomePageView(TemplateView):

    def get(self, request, *args, **kwargs):

        manufactures = Manufactures.objects.all()
        categories = Categories.objects.all()
        products = Products.objects.all()

        # return render(request, 'home.html', {'manufactures': manufactures, 'categories': categories, 'products': products})
        return render(request, 'home.html', {'manufactures': manufactures})