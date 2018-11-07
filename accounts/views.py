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

# def edit_profile(request):
#     if request.method == 'POST':
#         form = EditProfileForm(request.POST, instance=request.user)
#
#         if form.is_valid():
#             form.save()
#             return redirect(reverse('accounts:view_profile'))
#     else:
#         form = EditProfileForm(instance=request.user)
#         args = {'form': form}
#         return render(request, 'accounts/edit_profile.html', args)
#
# def change_password(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(data=request.POST, user=request.user)
#
#         if form.is_valid():
#             form.save()
#             update_session_auth_hash(request, form.user)
#             return redirect(reverse('accounts:view_profile'))
#         else:
#             return redirect(reverse('accounts:change_password'))
#     else:
#         form = PasswordChangeForm(user=request.user)
#
#         args = {'form': form}
#         return render(request, 'accounts/change_password.html', args)
