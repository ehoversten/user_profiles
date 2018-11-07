from django.shortcuts import render, redirect, HttpResponse
# from django.contrib.auth.forms import UserCreationForm
from accounts.forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

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

@login_required
def profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    context = {
        'user': user,
    }

    return render(request, 'accounts/profile.html', context)
