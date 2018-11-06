from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from home.forms import HomeForm
# Create your views here.


class HomeView(TemplateView):
    template_name = 'home/dashboard.html'


    def get(self, request):
        # initalize form instance
        form = HomeForm()
        context = {
            'form' : form

        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['post']
            print(text)
            form = HomeForm()
            
        context = {
            'form' : form,
            'text' : text,

        }
        return render(request, self.template_name, context)
