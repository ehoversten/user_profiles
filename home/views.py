from django.shortcuts import render, redirect
from django.views.generic import TemplateView
# Create your views here.
# def dashboard(request):
#     context = {
#
#     }
#     return render(request, 'home/dashboard.html', context)


class HomeView(TemplateView):
    template_name = 'home/dashboard.html'
