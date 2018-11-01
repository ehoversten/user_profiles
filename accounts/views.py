from django.shortcuts import render, redirect, HttpResponse
# from django.contrib.auth.forms import UserCreationForm
from accounts.forms import RegistrationForm
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    context = {

    }
    return render(request, 'accounts/index.html', context)


def register(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/accounts")

    else:
        # create an instance of the forms
        # form = UserCreationForm()
        form = RegistrationForm()


        context = {
            'form': form,
        }

        return render(request, "accounts/reg_form.html", context)

def profile(request):
    context = {
        'user': request.user
    }

    return render(request, 'accounts/profile.html', context)
