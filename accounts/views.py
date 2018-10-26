from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    context = {

    }
    return render(request, 'accounts/index.html', context)
